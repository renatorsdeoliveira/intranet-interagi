from pathlib import Path
from faker import Faker
import logging
import requests
from random import choice

fake = Faker("pt_BR")

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
session.headers.update(headers)

# Autenticar o usuário admin utilizando um Token JWT
login_url = f"{BASE_URL}/@login"
response = session.post(login_url, json={"login": USUARIO, "password": SENHA})
data = response.json()
token = data["token"]
session.headers.update(
    {"Authorization": f"Bearer {token}"}
)

# Criar pasta Time
data = {
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
}
response = session.get(f"{BASE_URL}/{data['id']}")
if response.status_code == 404:
    content = session.post(BASE_URL, json=data)


AREAS = [
    "/marketing",
    "/ti",
    "/ti/desenvolvimento"
]

PREDIOS = [
    "sede",
    "filial-01",
    "filial-02",
    "filial-03",
    "filial-04",
]

parent_url = f"{BASE_URL}/time"
for idx in range(1, 250):
    area = choice(AREAS)
    data = {
        "id": f"pessoa-{idx:02d}",
        "@type": "Pessoa",
        "title": fake.name(),
        "area": [{"@id": area}, ],
        "ramal": f"1{idx:03d}",
        "email": f"pessoa-{idx:02d}@plone.org",
        "predio": {"token": choice(PREDIOS)}
    }
    path = data['id']
    response = session.get(f"{parent_url}/{path}")
    if response.status_code != 404:
        logger.info(f"Ignorando {parent_url}/{path}: Conteúdo já existe")
        continue
    response = session.post(parent_url, json=data)
    if response.status_code > 300:
        logger.error(f"Erro ao criar '{path}': {response.status_code}")
    else:
        logger.info(f"Conteúdo criado: '{path}'")
