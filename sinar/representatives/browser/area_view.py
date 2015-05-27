from five import grok
from plone.directives import dexterity, form
from sinar.representatives.content.area import IArea

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IArea)
    grok.require('zope2.View')
    grok.template('area_view')
    grok.name('view')

