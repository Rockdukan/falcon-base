import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseModel


class Settings(BaseModel):
    """Прикладные настройки, читаемые из окружения."""
    APP_NAME: str = "falcon-base"
    DEBUG: bool = False


@lru_cache
def get_settings() -> Settings:
    """
    Возвращает singleton настроек после загрузки `.env`.

    Returns:
        Экземпляр `Settings`.
    """
    load_dotenv()

    return Settings(
        APP_NAME=os.environ.get("APP_NAME", "falcon-base"),
        DEBUG=os.environ.get("DEBUG", "false").lower() in ("1", "true", "yes", "on"),
    )
