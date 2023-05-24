from pathlib import Path
import logging
import requests
from random import choice

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

conteudos = [
    {
        "_parent": "/",
        "id": "time",
        "@type": "Document",
        "title": "Time",
        "description": "Nossa Equipe",
        "blocks": {
            "a10e3d32-d2b5-4442-923b-e1e5e720948c": {
            "@type": "title"
            },
            "52eb0f0d-6131-4696-a794-510bd086ebac": {
            "@type": "listing"
            }
        },
        "blocks_layout": {
            "items": [
            "a10e3d32-d2b5-4442-923b-e1e5e720948c",
            "52eb0f0d-6131-4696-a794-510bd086ebac"
            ]
        },
        "language": "pt-br",
        "subjects": [
            "Time",
            "RH"
        ]
    },
    {
        "_parent": "/",
        "id": "ti",
        "@type": "Area",
        "title": "TI",
        "description": "Tecnologia da Informação",
        "email": "ti@plone.org",
        "ramal": "1874",
    },
    {
        "_parent": "/ti/",
        "id": "desenvolvimento",
        "@type": "Area",
        "title": "Desenvolvimento",
        "description": "Tecnologia da Informação: Time de Desenvolvimento",
        "email": "dev@plone.org",
        "ramal": "1337",
    },
    {
        "_parent": "/",
        "id": "marketing",
        "@type": "Area",
        "title": "Marketing",
        "description": "Marketing",
        "email": "mktg@plone.org",
        "ramal": "3322",
    },
]
for conteudo in conteudos:
    parent = conteudo["_parent"]
    o_id = conteudo["id"]
    del conteudo["_parent"]
    parent_url = f"{BASE_URL}{parent}"
    response = session.get(f"{parent_url}{o_id}")
    if response.status_code == 404:
        response = session.post(parent_url, json=conteudo)
        content = response.json()
        logger.info(f"Conteúdo {content['@id']} criado")
