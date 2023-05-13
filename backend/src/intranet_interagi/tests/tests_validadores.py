from intranet_interagi import validadores

import pytest


@pytest.mark.parametrize(
    "value,expected",
    [
        ["1@plone.org", True],
        ["foobar@plone.org", True],
        ["bar-foo@plone.org", True],
        ["1@plone.org.br", False],
        ["foobar@plone.org.br", False],
        ["bar-foo@plone.org.br", False],
        ["ericof@simplesconsultoria.com.br", False],
    ]
)
def test_is_valid_email(value, expected):
    """Testa a função is_valid_email."""
    assert validadores.is_valid_email(value) is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        ["1234", True],
        ["4321", True],
        ["9234", True],
        [" ", False],
        ["12.34", False],
        ["HOLA", False],
        ["d1234", False],
        ["1234d", False],
    ]
)
def test_is_valid_extension(value, expected):
    """Testa a função is_valid_extension."""
    assert validadores.is_valid_extension(value) is expected
