from dotenv import load_dotenv
from typing import Optional
from flask import Flask
import os

# Cargamos las variables del entorno
load_dotenv


# Creamos la configuraciòn base
class Config(object):
    @staticmethod
    def init_app(app:Flask) -> None:
        pass
    SECRET_KEY:Optional[str] = os.getenv("FLASK_SECRET_KEY")


# Clase de desarrollo
class DevelopmentConfig(Config):
    ENV:str = "development"
    DEBUG:bool = True


# Clase de producciòn
class ProductionConfig(Config):
    ENV:str = "production"
    DEBUG:bool = False


# Diccionario con los objetos de Config
settings = {
    "development":DevelopmentConfig,
    "production":ProductionConfig,

    "default":DevelopmentConfig
}