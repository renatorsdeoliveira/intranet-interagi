from intranet_interagi.content.pessoa import IPessoa
from plone.indexer import indexer


@indexer(IPessoa)
def area_indexer(obj):
    areas = [area.to_object for area in obj.area]
    values = [area.UID() for area in areas]
    return values
