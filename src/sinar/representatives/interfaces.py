from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage

from sinar.representatives import _

class IRepresentative(form.Schema):
    """A conference presenter. Presenters can be added anywhere.
    """
    
    title = schema.TextLine(
            title=_(u"Name"),
            description=_(u'The name of the representative without'
                u'titles and honorifics.'
                u'eg. Dzulkefly Ahmad and not '
                u'Hj. Dzukkefly Ahmad'),
        )
    
    description = schema.Text(
            title=_(u"A short summary"),
            description=_(u'eg. An ex-lawyer who is now the'
            u'representative for Shah Alam'),
        )
    
    bio = RichText(
            title=_(u"Bio"),
            required=False
        )
    
    picture = NamedImage(
            title=_(u"Picture"),
            description=_(u"Please upload an image"),
            required=False,
        )

class IMP(IRepresentative):
    pass

