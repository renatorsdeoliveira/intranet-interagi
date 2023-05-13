import re


def is_valid_email(value: str) -> bool:
    """Validar se o email é @plone.org."""
    return value.endswith("@plone.org") if value else True


def is_valid_extension(value: str) -> bool:
    """Validar se o o ramal tem 4 dígitos numéricos."""
    return re.match(r"^\d{4}$", value) if value else True
