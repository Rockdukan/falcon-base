import falcon
from pydantic import ValidationError

from app.resources.base import BaseResource
from app.schemas.user import UserCreatePayload
from app.services import user as user_service


class UsersResource(BaseResource):
    """Коллекция пользователей: список и приём демонстрационного POST."""
    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        Возвращает пустой список пользователей (заготовка).

        Args:
            req: Запрос.
            resp: Ответ.
        """
        resp.media = {"items": []}


    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        Принимает JSON, валидирует через Pydantic, без записи в БД.

        Args:
            req: Запрос.
            resp: Ответ.

        Raises:
            falcon.HTTPBadRequest: При неверном теле запроса.
        """
        try:
            data = req.get_media() or {}
            payload = UserCreatePayload.model_validate(data)
        except ValidationError:
            raise falcon.HTTPBadRequest(description="Некорректное тело запроса")

        resp.status = falcon.HTTP_201
        resp.media = user_service.describe_user_payload(payload)
