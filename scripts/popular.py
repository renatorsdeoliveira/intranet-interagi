import logging
import requests


# Define como faremos o log das ações
logging.basicConfig()
logger = logging.getLogger("Interagi Popular")
logger.setLevel(logging.INFO)


# Constantes utilizadas no script
BASE_URL="http://localhost:8080/Plone/++api++"
USUARIO="admin"
SENHA="admin"
CONTEUDOS = {
    "/documentos": {
        "id": "documentos",
        "@type": "Document",
        "title": "Documentos da Organização",
        "blocks": {
            "a10e3d32-d2b5-4442-923b-e1e5e720948c": {
                "@type": "title"
            },
            "52eb0f0d-6131-4696-a794-510bd086ebac": {
                "@type": "listing"
            },
        },
        "blocks_layout": {
            "items": [
                "a10e3d32-d2b5-4442-923b-e1e5e720948c",
                "52eb0f0d-6131-4696-a794-510bd086ebac"
            ]
        },
        "language": "pt-br",
        "subjects": [
            "Documentos",
            "Arquivos"
        ]
    },
    "/documentos/norma-01": {
        "id": "norma-01",
        "@type": "Document",
        "title": "Norma 01",
        "blocks": {
            "C51A03C5-4D41-4364-8907-0BB32D845B0A": {
                "@type": "title"
            },
        },
        "blocks_layout": {
            "items": [
                "C51A03C5-4D41-4364-8907-0BB32D845B0A"
            ]
        },
        "language": "pt-br",
        "subjects": [
            "Documentos"
        ]
    },
}

# Cabeçalhos HTTP
headers = {
    "Accept": "application/json"
}

session = requests.Session()
session.headers.update(headers)

# Autenticar o usuário admin utilizando um Token JWT
login_url = f"{BASE_URL}/@login"
response = session.post(login_url, json={"login": USUARIO, "password": SENHA})
data = response.json()
token = data["token"]
session.headers.update(
    {"Authorization": f"Bearer {token}"}
)

# Criar documentos
for path, data in CONTEUDOS.items():
    id_conteudo = data["id"]
    # Obtem o caminho para o "pai" desse novo documento
    # /documentos/norma-001 -> /documentos
    # /documentos ->
    parent = path[:len(path) - len(id_conteudo) - 1]
    parent_url = f"{BASE_URL}{parent}"
    response = session.post(parent_url, json=data)
    if response.status_code > 300:
        logger.error(f"Erro ao criar '{path}': {response.status_code}")
    else:
        logger.info(f"Conteúdo criado: '{path}'")
