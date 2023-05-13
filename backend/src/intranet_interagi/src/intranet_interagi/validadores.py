from intranet_interagi import _
from zope.interface import Invalid

import re


class BadValue(Invalid):
    """Exception raised when a provided value is informed."""

    __doc__ = _("The value is not correct")


def do_validation(data):
    """Validate email set by the user."""
    value = data.email
    if not (value and is_valid_email(value)):
        raise BadValue(f"The email {value} is not in the plone domain.")


def is_valid_email(value: str) -> bool:
    """Validar se o email é @plone.org."""
    return value.endswith("@plone.org") if value else True


def is_valid_extension(value: str) -> bool:
    """Validar se o o ramal tem 4 dígitos numéricos."""
    return re.match(r"^\d{4}$", value) if value else True
