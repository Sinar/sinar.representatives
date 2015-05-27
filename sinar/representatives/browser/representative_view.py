from five import grok
from plone.directives import dexterity, form
from sinar.representatives.content.representative import IRepresentative

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IRepresentative)
    grok.require('zope2.View')
    grok.template('representative_view')
    grok.name('view')

