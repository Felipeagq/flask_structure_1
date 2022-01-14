from flask import Flask 
from .settings import settings
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv

# Cargamos las variables del entorno
load_dotenv()


# Creamos la funcion creadora de la app
def create_app(setting_name:str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(settings[setting_name])
    settings[setting_name].init_app(app)

    from .commom import error_handlers
    error_handlers(app)


    # from .routes.r1.route1 import route1
    # from .routes.r2.route2 import route2
    # route1(app)
    # route2(app)

    from app.routes.r2.route2 import r2_b
    app.register_blueprint(r2_b)

    return app