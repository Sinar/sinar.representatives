from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from collective import dexteritytextindexer
from collective.z3cform.widgets.token_input_widget import TokenInputFieldWidget

from sinar.representatives import _

class IRepresentative(form.Schema):
    """A conference presenter. Presenters can be added anywhere.
    """

    form.fieldset('websocial',
            label=u'Web and Social',
            fields=['url_website',
                    'url_wikipedia',
                    'url_blog',
                    'url_facebook',
                    'url_googleplus',
                    'url_twitter',
                    ]
            )

   
    title = schema.TextLine(
            title=_(u"Name"),
            description=_(u'The name of the representative without'
                u'titles and honorifics.'
                u'eg. Dzulkefly Ahmad not, '
                u'Hj. Dzukkefly Ahmad'),
        )

    description = schema.Text(
            title=_(u"A short summary"),
            description=_(u'eg. An ex-lawyer who is now the'
            u'representative for Shah Alam'),
            required=False,
        )
 
    honorifics = schema.TextLine(
            title=_(u"Honorifics"),
            description=_(u'Full honorifics eg. Y.A.B. Dato\' Sri'),
            required=False,
            )

    date_of_birth = schema.Date(
            title=_(u'Date of Birth'),
            required=False,
            )

    place_of_birth = schema.TextLine(
            title=_(u'Place of Birth'),
            description = _(u'eg. Subang Jaya, Selangor'),
            required=False,
            )

    current_spouses = schema.List(
            title = _(u'Current Spouse(s)'),
            description = _(
                u'Full name without honorifics. '
                'One per line.'),
            value_type=schema.TextLine(),
            required=False,
            )

    children = schema.List(
            title = _(u'Children'),
            description = _(u'Full name without honorifics. '
                'One per line.'),
            value_type=schema.TextLine(),
            required=False,
            )

    political_party = schema.List(
        title = _(u'Political Party'),
        description = _(u'eg. UMNO, 2007-present. One per line, latest first.'),
        value_type=schema.TextLine(),
        required=False,
        )

    education = RichText(
        title=_(u'Education'),
        description=_(u'Academic Background'),
        required=False,
        )

   
    working_experience = RichText(
        title=_(u"Work Experience"),
        description=_('eg. Position name, Company/Organization'
            '1998-1997. Latest first.'),
        required=False
    )

    political_experience = RichText(
        title=_(u"Political History"),
        description=_('eg. Head of PAS Research, PAS'
            '1998-1997. latest first.'),
        required=False
    )

    company_ownership = RichText(
        title=_(u"Company Ownership"),
        description=_('eg. Director, ABC Sdn Bhd'
            '1998-1997. latest first.'),
        required=False
    )

    assets = RichText(
        title=_(u"Known Assets, estimated value"),
        description=_('eg. House in Bukit Tunku, RM15 Million.'
            '[citation] '
            'Must have citation from reliable source.'),
        required=False
    )

    notes = RichText(
        title=_(u"Additional Notes"),
        description=_('Any other related notes.'),
        required=False
    )

    url_website = schema.TextLine(
            title=_(u'Personal website'),
            description=_('eg. http://www.google.com'),
            required=False
            )

    url_wikipedia= schema.TextLine(
            title=_(u'Wikipedia'),
            description=_('eg. http://www.wikipedia.org/RMS'),
            required=False
            )

    url_blog= schema.TextLine(
            title=_(u'Blog'),
            description=_('eg. http://www.blogger.com/RMS'),
            required=False
            )

    url_facebook= schema.TextLine(
            title=_(u'Facebook'),
            description=_('eg. http://www.facebook.com/profilename'),
            required=False
            )

    url_googleplus= schema.TextLine(
            title=_(u'Google Plus'),
            description=_('eg. http://plus.google.com/profilename'),
            required=False
            )

    url_twitter= schema.TextLine(
            title=_(u'Twitter'),
            description=_('eg. http://twitter.com/profilename'),
            required=False
            )

    email = schema.TextLine(
            title=_(u'Email address'),
            description=_(u'eg. kohtsukoon@pmo.gov.my'),
            required=False,
            )

    phone = schema.TextLine(
            title=_(u'Phone'),
            description=_(u'eg. +60 3 8888 8000'),
            required=False,
            )

    fax = schema.TextLine(
            title=_(u'Fax'),
            description=_(u'eg. +60 3 8888 8000'),
            required=False,
            )

    picture = NamedBlobImage(
            title=_(u"Picture"),
            description=_(u"Please upload an image"),
            required=False,
        )

class IMP(IRepresentative):

    parliamentary_constituency = schema.TextLine(
        title = _(u'Constituency'),
        description = _(u'Parliamentary constituencies. eg. Pagoh, P143 '
            'refer to '
            'http://en.wikipedia.org/wiki/List_of_Malaysian_electoral_districts'
            ),
        required=False,
        )

    parliamentary_portfolio = schema.List(
            title=_(u'Portfolio(s)'),
            description=_(u'eg. Minister of Education, 2008-present. '
                'One per line including past positions held'),
            value_type=schema.TextLine(),
            required=False,
            )
    pass

