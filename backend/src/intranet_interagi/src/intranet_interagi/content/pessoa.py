from intranet_interagi import _
from plone.dexterity.content import Container
from plone.schema.email import Email
from plone.supermodel import model
from plone.supermodel.model import Schema
from zope import schema
from zope.interface import implementer


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
    ramal = schema.TextLine(title=("Ramal"), required=False)


@implementer(IPessoa)
class Pessoa(Container):
    """Uma pessoa."""

