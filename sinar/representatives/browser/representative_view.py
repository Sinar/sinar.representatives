from five import grok
from plone.directives import dexterity, form
import requests
import datetime
import json
from dateutil import parser
from sinar.representatives.content.representative import IRepresentative

grok.templatedir('templates')

class View(dexterity.DisplayForm):
    grok.context(IRepresentative)
    grok.require('zope2.View')
    grok.template('representative_view')
    grok.name('view')

    def person(self):
       person_raw = requests.get(
               'https://sinar-malaysia.popit.mysociety.org/api/v0.1/persons/' + 
                self.context.popit_id)
       person_json = json.loads(person_raw.content)

       person = person_json['result']

       return person
