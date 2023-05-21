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
PASTA_DADOS = PASTA_ATUAL / "data"
BASE_URL="http://localhost:8080/Plone/++api++"
USUARIO="admin"
SENHA="admin"

arquivo_dados = PASTA_DADOS / "popular.json"
with open(arquivo_dados, "r") as fh:
    CONTEUDOS = json.load(fh)

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
    response = session.get(f"{BASE_URL}{path}")
    if response.status_code != 404:
        logger.info(f"Ignorando '{path}': Conteúdo já existe")
        continue
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
