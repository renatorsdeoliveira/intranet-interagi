from pathlib import Path
import json
import logging
import requests

# Define como faremos o log das ações
logging.basicConfig()
logger = logging.getLogger("Interagi Listagem")
logger.setLevel(logging.INFO)


# Constantes utilizadas no script
PASTA_ATUAL = Path(__file__).parent.resolve()
PASTA_DADOS = PASTA_ATUAL / "data"
BASE_URL = "https://api.open-meteo.com/v1/forecast"


def _formatar_resposta(data: dict) -> dict:
    """Parseia os dados obtidos da OpenMeteo.

       retorna um dicionários com informações meteorológicas.
    """
    dados_diarios = data["daily"]
    dados_hora = data["hourly"]
    sunrise = dados_diarios["sunrise"]
    sunset = dados_diarios["sunset"]
    horarios = dados_hora["time"]
    sequencia = dados_hora["temperature_2m"]
    temperatura = {hora: temp for hora, temp in zip(horarios, sequencia)}
    return {
        "sunrise": sunrise,
        "sunset": sunset,
        "temperature": temperatura
    }



def dados_clima(latitude: str, longitude: str, timezone: str) -> dict:
    """Chama o serviço Open Meteo e retorna os dados de clima."""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "timezone": timezone,
        "hourly": "temperature_2m",
        "daily": "sunrise,sunset",
        "forecast_days":1
    }
    response = requests.get(
        BASE_URL,
        params=params
    )
    data = response.json()
    return _formatar_resposta(data)


latitude, longitude = "-25.43", "-49.27"
timezone = "America/Sao_Paulo"
dados = dados_clima(latitude=latitude, longitude=longitude, timezone=timezone)

arquivo_dados = PASTA_DADOS / "meteo.json"
with open(arquivo_dados, "w") as fh:
    json.dump(dados, fh, indent=2)
    logger.info(f"Dados openmeteo salvos em {arquivo_dados}")
