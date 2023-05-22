from intranet_interagi import logger
from plone import api


def reindexa_pessoa(context):
    # Reindexa o campo area do tipo pessoa
    brains = api.content.find(portal_type="Pessoa")
    for brain in brains:
        pessoa = brain.getObject()
        pessoa.reindexObject(idxs=["area"])
        logger.info(f"- Reindexa o campo area do objeto {pessoa.absolute_url()}")
    logger.info("Reindexação completa")
