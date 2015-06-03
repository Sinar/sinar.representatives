from five import grok
from plone.directives import dexterity, form
from sinar.representatives.content.post import IPost
import json
import requests

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IPost)
    grok.require('zope2.View')
    grok.template('post_view')
    grok.name('view')

    def representative(self):

        popit_id = self.context.representative.to_object.popit_id

        person_raw = requests.get('http://sinar-malaysia.popit.mysociety.org/api/v0.1/search/persons?q=id:'
                + popit_id)

        person_json = json.loads(person_raw.content)

        person = person_json['result'][0]

        return person
