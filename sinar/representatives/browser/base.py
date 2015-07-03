from collective.portlet.collectionmultiview import BaseRenderer
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
from zope.interface import Interface
from zope import schema
from plone.app.form.widgets.wysiwygwidget import WYSIWYGWidget

class FeaturedRenderer(BaseRenderer):

    title = 'Featured Renderer'
    template = ViewPageTemplateFile('templates/featured.pt')
