from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE

import intranet_interagi


class INTRANET_INTERAGILayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=intranet_interagi)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "intranet_interagi:default")
        applyProfile(portal, "intranet_interagi:initial")


INTRANET_INTERAGI_FIXTURE = INTRANET_INTERAGILayer()


INTRANET_INTERAGI_INTEGRATION_TESTING = IntegrationTesting(
    bases=(INTRANET_INTERAGI_FIXTURE,),
    name="INTRANET_INTERAGILayer:IntegrationTesting",
)


INTRANET_INTERAGI_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(INTRANET_INTERAGI_FIXTURE, WSGI_SERVER_FIXTURE),
    name="INTRANET_INTERAGILayer:FunctionalTesting",
)


INTRANET_INTERAGIACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        INTRANET_INTERAGI_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name="INTRANET_INTERAGILayer:AcceptanceTesting",
)
