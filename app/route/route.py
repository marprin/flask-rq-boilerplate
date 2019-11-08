import rq_dashboard
from app.auth.views import auth


def register_route_blueprint(app):
    app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq-dashboard")
    app.register_blueprint(auth, url_prefix="/auth")
