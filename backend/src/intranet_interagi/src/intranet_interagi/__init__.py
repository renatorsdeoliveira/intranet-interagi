"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "intranet_interagi"

_ = MessageFactory("intranet_interagi")

logger = logging.getLogger("intranet_interagi")
