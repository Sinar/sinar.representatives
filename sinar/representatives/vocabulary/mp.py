from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource
from zope.interface import implements, alsoProvides
from zope.schema.interfaces import ITitledTokenizedTerm

import json
import requests

class mp(grok.GlobalUtility):
    """A queriable source for MPs.
    popit_ids are tokens and also values, title is name.
    """
    grok.name('sinar.representatives.mp')

    implements(IQuerySource)

    def __init__(self):
        pass
    
    def search(self, query_string):

        seen = set()

        popit_request = requests.get('http://sinar-malaysia.popit.mysociety.org/api/v0.1/search/persons?q=name:'
                + query_string)
        
        results = json.loads(popit_request.content)['result']

        for result in results:
            seen.add(result['id'])
            token = result['id']
            value = result['id']
            title = result['name']
