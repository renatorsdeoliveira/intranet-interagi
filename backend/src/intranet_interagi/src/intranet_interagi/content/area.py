from intranet_interagi import _
from intranet_interagi.validadores import is_valid_email
from intranet_interagi.validadores import is_valid_extension
from plone.dexterity.content import Container
from plone.schema.email import Email
from plone.supermodel import model
from plone.supermodel.model import Schema
from zope import schema
from zope.interface import implementer


class IArea(Schema):
    """Uma Area."""

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
    title = schema.TextLine(title=_("Nome da área"), required=True)
    description = schema.Text(title=_("Sumário"), required=False)
    email = Email(
        title=_("Email"),
        required=False,
        constraint=is_valid_email,
    )
    ramal = schema.TextLine(
        title=("Ramal"),
        required=False,
        constraint=is_valid_extension,
    )


@implementer(IArea)
class Area(Container):
    """Uma area."""
