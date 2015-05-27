from five import grok
from plone.directives import dexterity, form
from sinar.representatives.content.legislature import ILegislature

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(ILegislature)
    grok.require('zope2.View')
    grok.template('legislature_view')
    grok.name('view')

