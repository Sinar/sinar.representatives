from five import grok
from plone.directives import dexterity, form
from sinar.representatives.content.post import IPost

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IPost)
    grok.require('zope2.View')
    grok.template('post_view')
    grok.name('view')

