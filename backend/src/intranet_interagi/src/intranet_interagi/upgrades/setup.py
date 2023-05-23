from intranet_interagi import logger
from plone import api


PROFILE_ID = "collective.bookmarks:default"


def instala_bookmarks(context):
    setup_tool = api.portal.get_tool("portal_setup")
    setup_tool.runAllImportStepsFromProfile(f"profile-{PROFILE_ID}")
    logger.info("collective.bookmarks instalado")
