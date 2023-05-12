from intranet_interagi import logger
from plone import api


def atualiza_permissoes(context):
    # Update workflow security
    wf_tool = api.portal.get_tool("portal_workflow")
    wf_tool.updateRoleMappings()
    logger.info("Aplica novas permissões")
