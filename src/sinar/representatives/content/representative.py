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

from dateutil import parser

import requests,json,datetime

class IRepresentative(model.Schema):
    """ Marker interface and Dexterity Python Schema for Representative
    """

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

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


class RepresentativeView(BrowserView):
   
    def popitperson(self):

        language = ILanguage(self.context).get_language()

        person_raw = requests.get(
                'http://api.popit.sinarproject.org/' +
                language + '/persons/' + 
                self.context.popit_personid + '?minify=false')

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
                    contentFilter={"portal_type" : "Blacklist Criteria"})[0]
            return blacklist_criteria.getFolderContents()
        
        except:
            return None

    def cv(self):


        try:
            cv = self.context.listFolderContents(
                    contentFilter={"portal_type" : "CV"})[0]
            return cv.getFolderContents()
        
        except:
            return None


    def campaign_materials(self):

        try:

            materials = self.context.listFolderContents(
                    contentFilter={"portal_type" : "Campaign Materials"})[0]
            return materials.getFolderContents()

        except:

            return None

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
