import falcon


def require_json(req: falcon.Request, resp: falcon.Response, resource: object, params: dict) -> None:
    """
    Пример «before»-хука: для некоторых маршрутов требует Content-Type JSON.

    Args:
        req: Запрос.
        resp: Ответ.
        resource: Целевой ресурс.
        params: Параметры маршрута.

    Raises:
        falcon.HTTPUnsupportedMediaType: Если заголовок не `application/json`.
    """
    if req.method in ("POST", "PUT", "PATCH"):
        content_type = req.get_header("Content-Type") or ""

        if "application/json" not in content_type.lower():
            raise falcon.HTTPUnsupportedMediaType(description="Ожидается application/json")
