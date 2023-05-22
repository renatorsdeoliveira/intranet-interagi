from intranet_interagi import logger
from intranet_interagi.services.meteo import openmeteo
from plone import api
from plone.restapi.services import Service


class MeteoGet(Service):
    @property
    def coordinates(self) -> tuple:
        """Retorna latitude e longitude de Curitiba."""
        return ("-25.43", "-49.27")

    @property
    def timezone(self) -> str:
        return api.portal.get_registry_record("plone.portal_timezone")

    def reply(self):
        portal = api.portal.get()
        portal_url = portal.absolute_url()
        latitude, longitude = self.coordinates
        timezone = self.timezone
        dados = openmeteo.dados_clima(latitude, longitude, timezone)
        dados["@id"] = f"{portal_url}/@meteo"
        logger.info("Retorna dados do clima")
        return dados
