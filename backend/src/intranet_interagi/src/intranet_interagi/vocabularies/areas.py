from plone import api
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


@provider(IVocabularyFactory)
def areas_vocabulary(context):
    """Vocabulary de area."""
    terms = []
    brains = api.content.find(portal_type="Area")
    for brain in brains:
        terms.append(SimpleTerm(brain.UID, brain.UID, brain.Title))
    return SimpleVocabulary(terms)
