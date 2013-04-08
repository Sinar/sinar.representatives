from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from collective import dexteritytextindexer
from plone.autoform.interfaces import IFormFieldProvider
from collective.z3cform.widgets.token_input_widget import \
TokenInputFieldWidget
from plone.formwidget.autocomplete import AutocompleteFieldWidget
from plone.app.dexterity.behaviors.metadata import IBasic


from sinar.representatives import _

class IRepresentative(form.Schema,IBasic):
    """A Parliamentary Representative.
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

    dexteritytextindexer.searchable('title')
    title = schema.TextLine(
            title=_(u"Name"),
            description=_(u'The name of the representative without'
                u'titles and honorifics.'
                u'eg. Dzulkefly Ahmad not, '
                u'Hj. Dzukkefly Ahmad'),
        )

    dexteritytextindexer.searchable('description')
    description = schema.Text(
            title=_(u"A short summary"),
            description=_(u'eg. An ex-lawyer who is now the '
            u'representative for Shah Alam'),
            required=False,
        )
 
    honorifics = schema.TextLine(
            title=_(u"Honorifics"),
            description=_(u'Full honorifics eg. Y.A.B. Dato\' Sri'),
            required=False,
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

    dexteritytextindexer.searchable('office_address')
    office_address = schema.Text(
            title=_(u'Office Address'),
            description = _(
                u'Street address of office'),
            required=False,
            )

    date_of_birth = schema.Date(
            title=_(u'Date of Birth'),
            required=False,

            )
    dexteritytextindexer.searchable('place_of_birth')
    place_of_birth = schema.TextLine(
            title=_(u'Place of Birth (Optional)'),
            description = _(u'eg. Subang Jaya, Selangor'),
            required=False,
            )
    dexteritytextindexer.searchable('place_of_residence')
    place_of_residence = schema.TextLine(
            title=_(u'Place of Residence'),
            description = _(u'eg. Subang Jaya, Selangor'),
            required=False,
            )
    dexteritytextindexer.searchable('current_spouses')
    current_spouses = schema.List(
            title = _(u'Current Spouse(s) (Optional)'),
            description = _(
                u'Full name without honorifics. '
                'One per line.'),
            value_type=schema.TextLine(),
            required=False,
            )
    dexteritytextindexer.searchable('children')
    children = schema.List(
            title = _(u'Adult Children (Optional)'),
            description = _(u'Full name without honorifics. '
                'One per line. '
                'Names of minors are strictly not allowed. '
                'Only if publicly shared by MP, '
                'running a business or in the news.'),
            value_type=schema.TextLine(),
            required=False,
            )

    dexteritytextindexer.searchable('political_experience')
    political_party = schema.List(
        title = _(u'Political Party'),
        description = _(u'eg. UMNO, 2007-present. One per line, latest first.'),
        value_type=schema.TextLine(),
        required=False,
        )

    dexteritytextindexer.searchable('education')
    education = RichText(
        title=_(u'Education'),
        description=_(u'Academic Background'),
        required=False,
        )

    dexteritytextindexer.searchable('working_experience')
    working_experience = RichText(
        title=_(u"Work Experience"),
        description=_('eg. Position name, Company/Organization'
            '1998-1997. Latest first.'),
        required=False
    )

    dexteritytextindexer.searchable('political_experience')
    political_experience = RichText(
        title=_(u"Political History"),
        description=_(u'eg. Head of PAS Research, PAS'
            '1998-1997. latest first.'),
        required=False
    )

    dexteritytextindexer.searchable('legal_cases')
    legal_cases= RichText(
        title=_(u'Legal Cases Filed (Optional)'),
        description=_(u'Cases filed by and against this '
        'respresentative. '
        'eg.  Charged for cheating in relation to the Port Klang'
        'Free Zone, July 2010'
        ),
        required=False
     )

    dexteritytextindexer.searchable('company_ownership')
    company_ownership = RichText(
        title=_(u"Company Ownership (Optional)"),
        description=_('eg. Director, ABC Sdn Bhd, '
            '1998-1997. latest first.'),
        required=False
    )

    dexteritytextindexer.searchable('assets')
    assets = RichText(
        title=_(u"Known Assets, estimated value (Optional)"),
        description=_('eg. House in Bukit Tunku, RM15 Million.'
            '[citation] '
            'Must have citation from reliable source.'),
        required=False
    )

    transparency_integrity = schema.Bool(
                title = _(u'Signed Election Pledge on Integrity'),
                )

    dexteritytextindexer.searchable('notes')
    notes = RichText(
        title=_(u"Sources and Additional Notes"),
        description=_('Sources and any other related information.'),
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

    picture = NamedBlobImage(
            title=_(u"Picture"),
            description=_(u"Please upload an image"),
            required=False,
        )


class IMP(IRepresentative):

    dexteritytextindexer.searchable('parliamentary_constituency')
    parliamentary_constituency = schema.TextLine(
        title = _(u'Constituency'),
        description = _(u'Parliamentary constituencies. eg. Pagoh, P143 '
            'refer to '
            'http://en.wikipedia.org/wiki/List_of_Malaysian_electoral_districts'),
        required=False,
        )

    dexteritytextindexer.searchable('parliamentary_portfolio')
    parliamentary_portfolio = schema.List(
            title=_(u'Portfolio(s)'),
            description=_(u'eg. Minister of Education, 2008-present. '
                'One per line including past positions held'),
            value_type=schema.TextLine(),
            required=False,
            )

