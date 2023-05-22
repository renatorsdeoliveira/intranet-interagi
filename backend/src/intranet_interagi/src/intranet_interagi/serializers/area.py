from intranet_interagi.content.area import IArea
from plone.restapi.interfaces import ISerializeToJson
from plone.restapi.interfaces import ISerializeToJsonSummary
from plone.restapi.serializer.converters import json_compatible
from plone.restapi.serializer.dxcontent import SerializeFolderToJson
from zope.component import adapter
from zope.component import getMultiAdapter
from zope.interface import implementer
from zope.interface import Interface


@implementer(ISerializeToJson)
@adapter(IArea, Interface)
class AreaJSONSerializer(SerializeFolderToJson):
    def pessoas(self):
        pessoas = []
        for obj in self.context.pessoas:
            pessoas.append(
                getMultiAdapter((obj, self.request), ISerializeToJsonSummary)()
            )
        pessoas = sorted(pessoas, key=lambda x: x.get("title"))
        return pessoas

    def __call__(self, version=None, include_items=True):
        result = super().__call__(version, include_items)
        result.update(
            json_compatible(
                {
                    "pessoas": self.pessoas(),
                }
            )
        )
        return result
