import logging.config
import settings
from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.contrib.cache import RedisCache
from werkzeug.utils import import_string
from route.route import register_route_blueprint


def create_app():
    logging.config.dictConfig(import_string("settings.LOGGING_CONFIG"))
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(settings)

    app.cache = RedisCache(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
        password=settings.REDIS_PASSWORD,
    )

    Limiter(app, key_func=get_remote_address, default_limits=["50 per minute"])

    register_route_blueprint(app)

    return app


app = create_app()


@app.route("/health")
def health_check():
    return jsonify({"status": "ok"}), 200
