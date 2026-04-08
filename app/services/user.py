from app.schemas.user import UserCreatePayload


def describe_user_payload(payload: UserCreatePayload) -> dict:
    """
    Пример слоя сервиса: возвращает словарь для ответа API.

    Args:
        payload: Провалидированные данные.

    Returns:
        Тело для `resp.media`.
    """
    return {"email": str(payload.email), "detail": "Пользователь не сохранён (скелет)."}
