from intranet_interagi import logger
from plone import api
from random import randint


def login_handler(event):
    """Cria objeto Pessoa se esse não existir."""
    portal = api.portal.get()
    user = event.object
    username = user.getUserName()
    nome = user.getProperty("fullname") or username
    email = user.getProperty("email") or ""
    pasta_time = portal["time"]
    area_ti = portal["ti"]
    predio = "sede"
    with api.env.adopt_roles(["Manager"]):
        # Buscar por objeto Pessoa com o mesmo id do username
        brains = api.content.find(portal_type="Pessoa", getId=username)
        if brains:
            # Temos um resultado, então ignoramos o
            # restante do código
            brain = brains[0]
            # Dá permissão apenas se usuário não a tiver
            pessoa = brain.getObject()
            roles = api.user.get_roles(user=user, obj=pessoa)
            if "Owner" not in roles or "Editor" not in roles:
                api.user.grant_roles(user=user, obj=pessoa, roles=["Owner", "Editor"])
            logger.info(f"Objeto pessoa existe em {brain.getURL()}")
            return
        email = email if email.endswith("@plone.org") else "dummy@plone.org"
        # Cria objeto Pessoa
        dados = {
            "type": "Pessoa",
            "id": username,
            "title": nome,
            "ramal": f"{randint(1000, 9999)}",
            "predio": predio,
            "email": email,
        }
        pessoa = api.content.create(container=pasta_time, **dados)
        logger.info(f"Criado objeto pessoa em {pessoa.absolute_url()}")
        # Criar relação entre pessoa e area
        api.relation.create(pessoa, area_ti, "area")
        # Dar permissão de Owner no objeto Pessoa para o usuário
        api.user.grant_roles(user=user, obj=pessoa, roles=["Owner", "Editor"])
        logger.info(f"Usuário {username} com permissões em {pessoa.absolute_url()}")
