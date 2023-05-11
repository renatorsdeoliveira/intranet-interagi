"""Portal settings tests."""
from plone import api

import pytest


class TestPortalSettings:
    """Test that Portal configuration is correctly done."""

    @pytest.mark.parametrize(
            "setting,expected",
            [
                ["plone.default_language", "pt-br"],
                ["plone.email_charset", "utf-8"],
                ["plone.email_from_address", "teste@gmail.com"],
                ["plone.email_from_name", "Intranet Interagi"],
                ["plone.enable_sitemap", True],
                ["plone.portal_timezone", "America/Sao_Paulo"],
                ["plone.site_title", "Intranet Interagi"],
                ["plone.smtp_host", "localhost"],
                ["plone.smtp_port", 25],
                ["plone.twitter_username", "https://twitter.com/home"],
            ]
    )
    def test_portal_settings(self, portal, setting, expected):
        """Test portal smtp_host."""
        value = api.portal.get_registry_record(setting)
        assert value == expected