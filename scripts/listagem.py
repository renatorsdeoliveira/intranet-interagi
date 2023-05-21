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
BASE_URL="http://localhost:8080/Plone/++api++"
USUARIO="admin"
SENHA="admin"

# Cria a pasta de dados caso ela não exista ainda
if not PASTA_DADOS.exists():
    PASTA_DADOS.mkdir(parents=True, exist_ok=True)
    logger.info(f"Criada a pasta {PASTA_DADOS}")

# Cabeçalhos HTTP
headers = {
    "Accept": "application/json"
}

session = requests.Session()
session.headers.update(headers)

# Autenticar o usuário admin utilizando um Token JWT
# Ref: https://6.docs.plone.org/plone.restapi/docs/source/usage/authentication.html
login_url = f"{BASE_URL}/@login"
response = session.post(login_url, json={"login": USUARIO, "password": SENHA})

## Checar se temos uma resposta válida
if not response.status_code == 200:
    raise ValueError("Usuário ou senha incorretos")
data = response.json()
token = data["token"]
session.headers.update(
    {"Authorization": f"Bearer {token}"}
)

# Acessar a raiz do portal
## Ref: https://6.docs.plone.org/plone.restapi/docs/source/usage/content.html#reading-a-resource-with-get
response = session.get(BASE_URL)
data = response.json()
titulo = data["title"]
logger.info(f"O título do portal é {titulo}")

# Listagem de todos os conteúdos no portal, ordenados pelo caminho
## Ref: https://6.docs.plone.org/plone.restapi/docs/source/endpoints/searching.html#search
search_url = f"{BASE_URL}/@search?sort_on=path"
response = session.get(BASE_URL)
data = response.json()
total_conteudo = data["items_total"]
logger.info(f"O portal conta com {total_conteudo} itens de conteúdo")


# Salvar os dados recebidos do portal em um arquivo json
arquivo_dados = PASTA_DADOS / "listagem.json"
with open(arquivo_dados, "w") as fh:
    json.dump(data, fh, indent=2)
    logger.info(f"Dados da listagem salvos em {arquivo_dados}")