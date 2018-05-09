# -*- coding: utf-8 -*-
from sinar.representatives.content.parliamentary_seat import IParliamentarySeat  # NOQA E501
from sinar.representatives.testing import SINAR_REPRESENTATIVES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


try:
    from plone.dexterity.schema import portalTypeToSchemaName
except ImportError:
    # Plone < 5
    from plone.dexterity.utils import portalTypeToSchemaName


class ParliamentarySeatIntegrationTest(unittest.TestCase):

    layer = SINAR_REPRESENTATIVES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Parliamentary Seat')
        schema = fti.lookupSchema()
        self.assertEqual(IParliamentarySeat, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Parliamentary Seat')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Parliamentary Seat')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IParliamentarySeat.providedBy(obj),
            u'IParliamentarySeat not provided by {0}!'.format(
                obj,
            ),
        )

    def test_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Parliamentary Seat',
            id='parliamentary_seat',
        )
        self.assertTrue(
            IParliamentarySeat.providedBy(obj),
            u'IParliamentarySeat not provided by {0}!'.format(
                obj.id,
            ),
        )
