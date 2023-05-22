from intranet_interagi import logger


def catch_all(event):
    klass_name = event.__class__
    atributos = ", ".join([attr for attr in dir(event) if not attr.startswith("_")])
    logger.info(f"EVENTO: {klass_name} - {atributos}")
