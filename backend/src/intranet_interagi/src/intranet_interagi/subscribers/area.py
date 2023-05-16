from intranet_interagi import logger
from intranet_interagi.content.area import Area
from plone import api
from zope.lifecycleevent import ObjectAddedEvent
from zope.lifecycleevent import ObjectModifiedEvent


def _update_exclude_from_nav(obj: Area):
    """Update exclude_from_nav in the Area object."""
    predio = obj.predio
    obj.exclude_from_nav = False if predio else True
    logger.info(f"Atualizado o campo exclude_from_nav para {obj.title}")


def _create_user_groups(obj: Area):
    """Create user groups for the new Area."""
    uid = api.content.get_uuid(obj)
    title = obj.title
    payload = {
        "groupname": f"{uid}_editors",
        "title": f"Editores para {title}",
        "description": f"Students for the {title} session",
    }
    editors = api.group.create(**payload)
    api.group.grant_roles(group=editors, roles=["Editor"], obj=obj)
    logger.info(
        f"Granted role of Editor to {uid}_editors group on {obj.absolute_url()}"
    )


def added(obj: Area, event: ObjectAddedEvent):
    """Post creation handler for Area."""
    _update_exclude_from_nav(obj)
    _create_user_groups(obj)


def modified(obj: Area, event: ObjectModifiedEvent):
    """Post edit handler for Area."""
    _update_exclude_from_nav(obj)
