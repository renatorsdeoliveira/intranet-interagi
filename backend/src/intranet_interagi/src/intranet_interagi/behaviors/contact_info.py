from intranet_interagi import _
from intranet_interagi.validadores import is_valid_email
from intranet_interagi.validadores import is_valid_extension
from plone.autoform.interfaces import IFormFieldProvider
from plone.schema.email import Email
from plone.supermodel import model
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IContactInfo(model.Schema):
    """Informações de contato."""

    model.fieldset("contact", label=_("Contact"), fields=["email", "ramal"])
    email = Email(
        title=_("Email"),
        required=False,
        constraint=is_valid_email,
    )

    ramal = schema.TextLine(
        title=_(
            "Ramal",
        ),
        required=False,
        constraint=is_valid_extension,
    )
