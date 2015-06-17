from five import grok
from plone.directives import dexterity, form
from sinar.representatives.content.post import IPost
import json
import datetime
from dateutil import parser
import requests

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IPost)
    grok.require('zope2.View')
    grok.template('post_view')
    grok.name('view')

    def representative(self):

        popit_id = self.context.representative.to_object.popit_id
        person_raw = requests.get('http://sinar-malaysia.popit.mysociety.org/api/v0.1/persons/' +
                     popit_id)

        person_json = json.loads(person_raw.content)
        person = person_json['result']

        if person.has_key('birth_date'):
            birth_date = person['birth_date']
            born = parser.parse(birth_date)
            today = datetime.date.today()
            age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))            
            person['age'] = age

        
        return person
