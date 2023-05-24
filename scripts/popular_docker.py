from pathlib import Path

import json
import logging
import requests


# Define como faremos o log das ações
logging.basicConfig()
logger = logging.getLogger("Interagi Popular")
logger.setLevel(logging.INFO)


# Constantes utilizadas no script
PASTA_ATUAL = Path(__file__).parent.resolve()
BASE_URL="http://127.0.0.1/++api++"
USUARIO="admin"
SENHA="admin"

# Cabeçalhos HTTP
headers = {
    "Accept": "application/json",
    "Host": "intranet.localhost"
}

session = requests.Session()
session.auth = (USUARIO, SENHA)
session.headers.update(headers)

with open(PASTA_ATUAL / "data" / "conteudos.json", "r") as fh:
    conteudos = json.load(fh)

for conteudo in conteudos:
    parent = conteudo["_parent"]
    o_id = conteudo["id"]
    del conteudo["_parent"]
    parent_url = f"{BASE_URL}{parent}"
    content_url = f"{parent_url}{o_id}"
    response = session.get(content_url)
    if response.status_code == 404:
        response = session.post(parent_url, json=conteudo)
        content = response.json()
        logger.info(f"Conteúdo {content['@id']} criado")
    elif response.status_code == 200:
        response = session.patch(content_url, json=conteudo)
        logger.info(f"Conteúdo {content_url} atualizado")
