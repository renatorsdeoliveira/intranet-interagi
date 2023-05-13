from intranet_interagi import logger
from intranet_interagi.content.area import Area
from zope.lifecycleevent import ObjectAddedEvent


def _update_excluded_from_nav(obj: Area):
    """Update excluded_from_nav in the Area object."""
    predio = obj.predio
    obj.excluded_from_nav = False if predio else True
    logger.info(f"Atualizado o campo excluded_from_nav para {obj.title}")


def added(obj: Area, event: ObjectAddedEvent):
    """Post creation handler for Area."""
    _update_excluded_from_nav(obj)
