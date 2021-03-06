# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from z3c.relationfield.schema import RelationList
from zope.interface import implementer
from plone.dexterity.browser.view import DefaultView
from sinar.representatives import _


class IParliamentarySeat(model.Schema):
    """ Marker interface and Dexterity Python Schema for ParliamentarySeat
    """

    representative = RelationList(
        title=_(u'Representative'),
        required=False,
        )

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    # text = RichText(
    #     title=_(u'Text'),
    #     required=False
    # )

    # url = schema.URI(
    #     title=_(u'Link'),
    #     required=False
    # )

    # fieldset('Images', fields=['logo', 'advertisement'])
    # logo = namedfile.NamedBlobImage(
    #     title=_(u'Logo'),
    #     required=False,
    # )

    # advertisement = namedfile.NamedBlobImage(
    #     title=_(u'Advertisement (Gold-sponsors and above)'),
    #     required=False,
    # )

    # directives.read_permission(notes='cmf.ManagePortal')
    # directives.write_permission(notes='cmf.ManagePortal')
    # notes = RichText(
    #     title=_(u'Secret Notes (only for site-admins)'),
    #     required=False
    # )

class ParliamentarySeatView(DefaultView):

    def representatives(self):

        representatives = self.context.representative

        persons = []

        for representative in representatives:
          
            obj = representative.to_object

            person = obj.Subject
            
            persons.append(person) 

        return persons

@implementer(IParliamentarySeat)
class ParliamentarySeat(Container):
    """
    """
