# -*- coding: utf-8 -*-
from sinar.representatives.content.representative import IRepresentative
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from sinar.representatives.testing import SINAR_REPRESENTATIVES_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class RepresentativeIntegrationTest(unittest.TestCase):

    layer = SINAR_REPRESENTATIVES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='representative')
        schema = fti.lookupSchema()
        self.assertEqual(IRepresentative, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='representative')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='representative')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IRepresentative.providedBy(obj))

    def test_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='representative',
            id='representative',
        )
        self.assertTrue(IRepresentative.providedBy(obj))
