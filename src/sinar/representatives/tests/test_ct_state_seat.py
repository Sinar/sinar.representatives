# -*- coding: utf-8 -*-
from sinar.representatives.content.state_seat import IStateSeat  # NOQA E501
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


class StateSeatIntegrationTest(unittest.TestCase):

    layer = SINAR_REPRESENTATIVES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='State Seat')
        schema = fti.lookupSchema()
        self.assertEqual(IStateSeat, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='State Seat')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='State Seat')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IStateSeat.providedBy(obj),
            u'IStateSeat not provided by {0}!'.format(
                obj,
            ),
        )

    def test_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='State Seat',
            id='state_seat',
        )
        self.assertTrue(
            IStateSeat.providedBy(obj),
            u'IStateSeat not provided by {0}!'.format(
                obj.id,
            ),
        )
