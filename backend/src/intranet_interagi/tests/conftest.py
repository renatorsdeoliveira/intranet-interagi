from intranet_interagi.testing import INTRANET_INTERAGI_INTEGRATION_TESTING
from pytest_plone import fixtures_factory


pytest_plugins = ["pytest_plone"]


globals().update(fixtures_factory(((INTRANET_INTERAGI_INTEGRATION_TESTING, "integration"),)))
