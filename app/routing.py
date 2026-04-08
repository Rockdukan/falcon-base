import falcon

from app.resources.health import HealthResource
from app.resources.user import UsersResource


def register_routes(app: falcon.App) -> None:
    """
    Регистрирует маршруты API.

    Args:
        app: Экземпляр Falcon-приложения.
    """
    app.add_route("/api/v1/health", HealthResource())
    app.add_route("/api/v1/users", UsersResource())
