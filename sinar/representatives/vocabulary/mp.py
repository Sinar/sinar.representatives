from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class mp(grok.GlobalUtility):
    grok.name('sinar.representatives.mp')
    grok.implements(IVocabularyFactory)

    _terms = [{
        'value': 'termvalue',
        'title': 'Term Title',
        'token': 'termtoken',
    }]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(*i))
        return SimpleVocabulary(terms)
