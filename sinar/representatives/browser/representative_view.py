from five import grok
from plone.directives import dexterity, form
import requests
import datetime
import json
from dateutil import parser

from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
from zc.relation.interfaces import ICatalog

from sinar.representatives.content.representative import IRepresentative

grok.templatedir('templates')

class View(dexterity.DisplayForm):
    grok.context(IRepresentative)
    grok.require('zope2.View')
    grok.template('representative_view')
    grok.name('view')

    def person(self):
       
        person_raw = requests.get(
               'http://sinar-malaysia.popit.mysociety.org/api/v0.1/persons/' + 
                self.context.popit_id)
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

    def mp_post(self):
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
