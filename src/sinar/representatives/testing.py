# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import sinar.representatives


class SinarRepresentativesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=sinar.representatives)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'sinar.representatives:default')


SINAR_REPRESENTATIVES_FIXTURE = SinarRepresentativesLayer()


SINAR_REPRESENTATIVES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SINAR_REPRESENTATIVES_FIXTURE,),
    name='SinarRepresentativesLayer:IntegrationTesting',
)


SINAR_REPRESENTATIVES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SINAR_REPRESENTATIVES_FIXTURE,),
    name='SinarRepresentativesLayer:FunctionalTesting',
)


SINAR_REPRESENTATIVES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SINAR_REPRESENTATIVES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SinarRepresentativesLayer:AcceptanceTesting',
)
