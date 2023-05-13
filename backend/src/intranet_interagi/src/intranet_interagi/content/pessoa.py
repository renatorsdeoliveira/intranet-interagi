from intranet_interagi import _
from intranet_interagi.validadores import do_validation
from intranet_interagi.validadores import is_valid_extension
from plone.dexterity.content import Container
from plone.schema.email import Email
from plone.supermodel import model
from plone.supermodel.model import Schema
from zope import schema
from zope.interface import implementer
from zope.interface import invariant


class IPessoa(Schema):
    """Uma Pessoa."""

    model.fieldset(
        "default",
        _("Default"),
        fields=[
            "title",
            "description",
            "email",
            "ramal",
        ],
    )

    # Basic info
    title = schema.TextLine(title=_("Nome Completo"), required=True)
    description = schema.Text(title=_("Bio"), required=False)
    email = Email(title=_("Email"), required=False)
    ramal = schema.TextLine(
        title=("Ramal"),
        required=False,
        constraint=is_valid_extension,
    )

    @invariant
    def validate_email(data):
        """Validate email set by the user."""
        do_validation(data)


@implementer(IPessoa)
class Pessoa(Container):
    """Uma pessoa."""
