from flask import Flask
from werkzeug.contrib.cache import RedisCache
from app.auth.views import auth
import settings
import logging.config
from werkzeug.utils import import_string


def create_app():
    logging.config.dictConfig(import_string('settings.LOGGING_CONFIG'))
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(settings)

    app.cache = RedisCache(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

    # Register blueprint here
    app.register_blueprint(auth)

    return app
