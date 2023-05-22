from intranet_interagi import _
from plone.app.vocabularies.catalog import StaticCatalogVocabulary
from plone.dexterity.content import Container
from plone.supermodel.model import Schema
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope import schema
from zope.interface import implementer


class IPessoa(Schema):
    """Uma Pessoa."""

    # Basic info
    title = schema.TextLine(title=_("Nome Completo"), required=True)
    description = schema.Text(title=_("Bio"), required=False)

    area = RelationList(
        title=_("pessoa_area", default="Area"),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_("pessoa_area", default="Area"),
            vocabulary=StaticCatalogVocabulary(
                {
                    "portal_type": ["Area"],
                }
            ),
        ),
    )


@implementer(IPessoa)
class Pessoa(Container):
    """Uma pessoa."""
