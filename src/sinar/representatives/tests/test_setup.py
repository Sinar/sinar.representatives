# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from sinar.representatives.testing import SINAR_REPRESENTATIVES_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that sinar.representatives is properly installed."""

    layer = SINAR_REPRESENTATIVES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if sinar.representatives is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'sinar.representatives'))

    def test_browserlayer(self):
        """Test that ISinarRepresentativesLayer is registered."""
        from sinar.representatives.interfaces import (
            ISinarRepresentativesLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ISinarRepresentativesLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SINAR_REPRESENTATIVES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['sinar.representatives'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if sinar.representatives is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'sinar.representatives'))

    def test_browserlayer_removed(self):
        """Test that ISinarRepresentativesLayer is removed."""
        from sinar.representatives.interfaces import \
            ISinarRepresentativesLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           ISinarRepresentativesLayer,
           utils.registered_layers())
