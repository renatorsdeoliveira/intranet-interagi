from intranet_interagi import _
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


PREDIOS = [
    ("sede", _("Edifício Sede")),
    ("filial-01", _("Filial 01")),
    ("filial-02", _("Filial 02")),
    ("filial-03", _("Filial 03")),
    ("filial-04", _("Filial 04")),
]


@provider(IVocabularyFactory)
def predios_vocabulary(context):
    """Vocabulário de possíveis prédios."""
    terms = []
    for id_, title in PREDIOS:
        terms.append(SimpleTerm(id_, id_, title))
    return SimpleVocabulary(terms)
