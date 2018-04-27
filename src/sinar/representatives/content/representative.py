# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from Products.CMFPlone.interfaces import ILanguage
from sinar.representatives import _

from plone import api
from Products.Five import BrowserView
from plone.dexterity.browser.view import DefaultView

from dateutil import parser

import requests,json,datetime

from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
from zc.relation.interfaces import ICatalog
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

political_party = SimpleVocabulary([
        SimpleTerm(value=u'bn', title=_(u'Barisan Nasional')),
        SimpleTerm(value=u'pkr', title=_(u'Parti Keadilan Rakyat')),
        SimpleTerm(value=u'psm', title=_(u'Parti Sosialis Malaysia')),
        SimpleTerm(value=u'pas', title=_(u'Parti Islam Se-Malaysia')),
        SimpleTerm(value=u'warisan', title=_(u'Warisan')),]
        )

logo = SimpleVocabulary([
        SimpleTerm(value=u'bn', title=_(u'Barisan Nasional')),
        SimpleTerm(value=u'pkr', title=_(u'Parti Keadilan Rakyat')),
        SimpleTerm(value=u'psm', title=_(u'Parti Sosialis Malaysia')),
        SimpleTerm(value=u'pas', title=_(u'Parti Islam Se-Malaysia')),
        SimpleTerm(value=u'warisan', title=_(u'Warisan')),]
        )

class IRepresentative(model.Schema):
    """ Marker interface and Dexterity Python Schema for Representative
    """

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    political_party = schema.Choice(
            title = _(u'Mewakili Parti Politik'),
            vocabulary = political_party,
            required=False,
            )

    logo = schema.Choice(
            title = _(u'Logo Party'),
            vocabulary = logo,
            required=False,
            )



    promises = RichText(
         title=_(u'Ucapan dan Janji'),
         required=False
     )

    # text = RichText(
    #     title=_(u'Text'),
    #     required=False
    # )

    # url = schema.URI(
    #     title=_(u'Link'),
    #     required=False
    # )

    # fieldset('Images', fields=['logo', 'advertisement'])
    # logo = namedfile.NamedBlobImage(
    #     title=_(u'Logo'),
    #     required=False,
    # )

    # advertisement = namedfile.NamedBlobImage(
    #     title=_(u'Advertisement (Gold-sponsors and above)'),
    #     required=False,
    # )

    # directives.read_permission(notes='cmf.ManagePortal')
    # directives.write_permission(notes='cmf.ManagePortal')
    # notes = RichText(
    #     title=_(u'Secret Notes (only for site-admins)'),
    #     required=False
    # )


class RepresentativeView(DefaultView):
   
    def popitperson(self):

        language = ILanguage(self.context).get_language()

        person_raw = requests.get(
                'http://api.popit.sinarproject.org/' +
                language + '/persons/' + 
                self.context.popit_personid)

        person_json = json.loads(person_raw.content)

        try:
           person = person_json['result']

           if person.has_key('birth_date'):
               if person['birth_date']:
                   birth_date = person['birth_date']
                   born = parser.parse(birth_date)
                   today = datetime.date.today()
                   age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))            
                   person['age'] = age

        except:
            print "Popit Error: " + person_json['errors'][0]
            person = None

        return person

    def blacklist_criteria(self):

        try:
            blacklist_criteria = self.context.listFolderContents(
                    contentFilter={"portal_type" : "Blacklist Criteria"})
            return blacklist_criteria
        
        except:
            return None

    def cv(self):

        try:
            cv = self.context.listFolderContents(
                    contentFilter={"portal_type" : "CV"})
            return cv
        
        except:
            return None


    def campaign_materials(self):

        try:

            materials = self.context.listFolderContents(
                    contentFilter={"portal_type" : "Campaign Materials"})[0]
            return materials.getFolderContents()

        except:

            return None


    def seats(self):
        """
        Return back references from source object on specified attribute_name
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)
    
        source_object = self.context
        attribute_name = 'representative'

        result = []

        for rel in catalog.findRelations(
                    dict(to_id=intids.getId(aq_inner(source_object)),
                    from_attribute=attribute_name)
                ):
            obj = intids.queryObject(rel.from_id)

            if obj is not None and checkPermission('zope2.View', obj):
                result.append(obj)

        return result

    #unused
    def contracts(self):

        contract_raw = requests.get(
                '10.8.0.100:8000/director?popit_id=545e46025222837c2c05909d')

        contract_json = json.loads(contract_raw.content)

        try:
           contract = contract_json

        except:
            print "Popit Error: " + contract_json['errors'][0]
            contract = None

        return contract

@implementer(IRepresentative)
class Representative(Container):
    """
    """
