# Falcon Base

Минимальный шаблон **Falcon**-приложения: WSGI, middleware (CORS, лог запросов), health-check, обработка ошибок, **OpenAPI** (`app/openapi/openapi.yaml`), **Swagger UI** (`/docs`) и **ReDoc** (`/redoc`).

## Структура репозитория

```
├── app/                              # пакет приложения Falcon
│   ├── middleware/                   # обработка запроса/ответа до и после ресурса
│   ├── openapi/                      # каталог с YAML-описанием API
│   │   └── openapi.yaml
│   ├── resources/                    # обработчики HTTP-маршрутов
│   ├── schemas/                      # модели Pydantic (заготовка)
│   ├── errors.py
│   ├── __init__.py
│   └── routing.py
├── config/                           # настройки из переменных окружения
├── static/                           # файлы для раздачи как статика
│   └── swagger/                      # ресурсы Swagger UI (css, js)
├── templates/                        # HTML-шаблоны страниц /docs и /redoc
│   ├── swagger_index.html
│   └── redoc.html
├── tests/                            # pytest
├── wsgi.py
├── run.py
├── MANIFEST.in
├── env.example
├── pyproject.toml
├── requirements.txt
├── LICENSE
└── README.md
```

## ⚙️ Установка и запуск
#### uv
```bash
git clone https://gitverse.ru/Rockdukan/falcon-base.git
cd falcon-base
uv venv
uv sync
python run.py
```

#### venv
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

Скрипт **`run.py`** передаёт в Gunicorn **`BIND`** (хост:порт) и **`TIMEOUT`** (секунды на запрос воркера) из окружения; значения по умолчанию и пример — в **`env.example`**, для образа Docker — в **`Dockerfile`**.

## 🧪 Тестирование

```bash
uv run pytest -q
```

## Маршруты

| Метод и путь | Назначение |
|--------------|------------|
| `GET /openapi.yaml` | Спецификация OpenAPI (YAML) |
| `GET /openapi.json` | Та же спецификация (JSON) |
| `GET /docs` | Swagger UI |
| `GET /redoc` | ReDoc |
| `GET /api/v1/health` | `{"status": "ok"}` |

Настройки приложения — `config/settings.py`. Полный пример переменных окружения — `env.example` (включая `BIND` и `TIMEOUT` для `run.py`).
