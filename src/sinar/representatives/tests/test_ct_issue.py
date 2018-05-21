# -*- coding: utf-8 -*-
from sinar.representatives.content.issue import IIssue  # NOQA E501
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


class IssueIntegrationTest(unittest.TestCase):

    layer = SINAR_REPRESENTATIVES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_issue_schema(self):
        fti = queryUtility(IDexterityFTI, name='Issue')
        schema = fti.lookupSchema()
        self.assertEqual(IIssue, schema)

    def test_ct_issue_fti(self):
        fti = queryUtility(IDexterityFTI, name='Issue')
        self.assertTrue(fti)

    def test_ct_issue_factory(self):
        fti = queryUtility(IDexterityFTI, name='Issue')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IIssue.providedBy(obj),
            u'IIssue not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_issue_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Issue',
            id='issue',
        )
        self.assertTrue(
            IIssue.providedBy(obj),
            u'IIssue not provided by {0}!'.format(
                obj.id,
            ),
        )
