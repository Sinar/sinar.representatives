# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from zope import schema
from zope.interface import implementer
from Products.CMFPlone.interfaces import ILanguage
from sinar.representatives import _

from plone import api
from Products.Five import BrowserView
from plone.dexterity.browser.view import DefaultView

from dateutil import parser
import requests
import json
import datetime

from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
from zc.relation.interfaces import ICatalog
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

logo = SimpleVocabulary([
        SimpleTerm(value=u'bn', title=_(u'Barisan Nasional')),
        SimpleTerm(value=u'bjis', title=(u'Barisan Jemaah Islamiah \
                                           Se-Malaysia')),
        SimpleTerm(value=u'par', title=_(u'Parti Alternative Rakyat')),
        SimpleTerm(value=u'amanah', title=_(u'Parti Amanah Negara')),
        SimpleTerm(value=u'pbds', title=_(u'Parti Bansa Dayak Sarawak')),
        SimpleTerm(value=u'pbk', title=_(u'Parti Bumi Kenyalang')),
        SimpleTerm(value=u'pcm', title=_(u'Parti Cinta Malaysia')),
        SimpleTerm(value=u'pcs', title=_(u'Parti Cinta Sabah')),
        SimpleTerm(value=u'phrs', title=_(u'Parti Harapan Rakyat Sabah')),
        SimpleTerm(value=u'pkan', title=_(u'Parti Kerjasama Anak Negeri')),
        SimpleTerm(value=u'pms', title=_(u'Parti Maju Sabah')),
        SimpleTerm(value=u'pprs', title=_(u'Parti Perpaduan Rakyat Sabah')),
        SimpleTerm(value=u'prgjp', title=_(u'Parti Rakyat Gabungan \
                                             Jaksa Pendamai')),
        SimpleTerm(value=u'prn', title=_(u'Parti Reformasi Negeri')),
        SimpleTerm(value=u'ppsta', title=_(u'Parti Solidariti Tanah Airku')),
        SimpleTerm(value=u'pnp', title=_(u'Penang Front Party')),
        SimpleTerm(value=u'pprks', title=_(u'Pertubuhan Perpaduan \
                                             Rakyat Kebangsaan Sabah')),
        SimpleTerm(value=u'pbsm', title=_(u'Parti Bersama Malaysia')),
        SimpleTerm(value=u'pas', title=_(u'Parti Islam Se-Malaysia (PAS)')),
        SimpleTerm(value=u'pkr', title=_(u'Parti Keadilan Rakyat')),
        SimpleTerm(value=u'prm', title=_(u'Parti Rakyat Malaysia')),
        SimpleTerm(value=u'psm', title=_(u'Parti Sosialis Malaysia (PSM)')),
        SimpleTerm(value=u'dap', title=_(u'Parti Tindakan Demokratik (DAP)')),
        SimpleTerm(value=u'warisan', title=_(u'Warisan')),
        SimpleTerm(value=u'bebas-arnab', title=_(u'Bebas Arnab')),
        SimpleTerm(value=u'bebas-kapalterbang', title=_(u'Bebas Kapal \
                                                            Terbang')),
        SimpleTerm(value=u'bebas-buku', title=_(u'Bebas Buku')),
        SimpleTerm(value=u'bebas-cawan', title=_(u'Bebas Cawan')),
        SimpleTerm(value=u'bebas-gajah', title=_(u'Bebas Gajah')),
        SimpleTerm(value=u'bebas-ikan', title=_(u'Bebas Ikan')),
        SimpleTerm(value=u'bebas-pen', title=_(u'Bebas Pen')),
        SimpleTerm(value=u'bebas-kereta', title=_(u'Bebas Kereta')),
        SimpleTerm(value=u'bebas-kerusi', title=_(u'Bebas Kerusi')),
        SimpleTerm(value=u'bebas-kunci', title=_(u'Bebas Kunci')),
        SimpleTerm(value=u'bebas-rumah', title=_(u'Bebas Rumah')),
        SimpleTerm(value=u'bebas-telefon', title=_(u'Bebas Telefon')),
        SimpleTerm(value=u'bebas-traktor', title=_(u'Bebas Traktor')),
        SimpleTerm(value=u'bebas-udang', title=_(u'Bebas Udang'))],
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
            title=_(u'Mewakili Parti Politik'),
            vocabulary="sinar.plone.vocabularies.PoliticalParties",
            required=False,
            )

    logo = schema.Choice(
            title=(u'Logo Party'),
            vocabulary=logo,
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
                    age = today.year - born.year - (
                            (today.month, today.day) < (born.month, born.day))
                    person['age'] = age

        except:
            print "Popit Error: " + person_json['errors'][0]
            person = None

        return person

    def blacklist_criteria(self):

        try:
            blacklist_criteria = self.context.listFolderContents(
                    contentFilter={"portal_type": "Blacklist Criteria"})
            return blacklist_criteria

        except:
            return None

    def cv(self):

        try:
            cv = self.context.listFolderContents(
                    contentFilter={"portal_type": "CV"})
            return cv

        except:
            return None

    def campaign_materials(self):

        try:

            materials = self.context.listFolderContents(
                    contentFilter={"portal_type": "Campaign Materials"})[0]
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

        try:

            for rel in catalog.findRelations(
                        dict(to_id=intids.getId(aq_inner(source_object)),
                             from_attribute=attribute_name)
                    ):
                obj = intids.queryObject(rel.from_id)

                if obj is not None and checkPermission('zope2.View', obj):
                    result.append(obj)

            return result

        except:
            pass

    # unused
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
