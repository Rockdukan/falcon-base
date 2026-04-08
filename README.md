# Falcon Base — базовый шаблон для приложений на Falcon
Falcon — это минималистичный фреймворк для построения HTTP API и облачных микросервисов на Python.
Он хорошо подходит там, где важны компактность кода и предсказуемая производительность.
![screenshot](screenshot.jpg)

## 🔧 В шаблоне реализовано:
- Базовая структура проекта
- Конфигурация через `config/` и переменные окружения
- WSGI-приложение `falcon.App`, маршруты и ресурсы
- Middleware CORS и логирование запросов
- Примеры ресурсов `health` и `users` с JSON и Pydantic

## 📦 Структура проекта
```
├── app/
│   ├── middleware/
│   ├── resources/
│   ├── hooks/
│   ├── schemas/
│   ├── services/
│   ├── models/
│   ├── errors.py
│   └── routing.py
├── config/
├── tests/
├── wsgi.py
├── env.example
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## ⚙️ Установка и запуск
```bash
git clone https://gitverse.ru/Rockdukan/falcon-base.git
cd falcon-base
uv venv
uv sync  # ставит зависимости из pyproject.toml
gunicorn wsgi:app -b 127.0.0.1:8000
```

Если вы предпочитаете устанавливать зависимости из `requirements.txt`, можно сделать так:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
pip install gunicorn
gunicorn wsgi:app -b 127.0.0.1:8000
```

## 🧪 Тестирование
```bash
uv sync --extra dev
uv run pytest -q
```

## 🌐 Маршруты

- `GET /api/v1/health`  
  Простой health-check эндпоинт. Возвращает JSON:

  ```json
  {"status": "ok"}
  ```

- `GET /api/v1/users`  
  Возвращает JSON со списком пользователей (в скелете пустой список):

  ```json
  {"items": []}
  ```

- `POST /api/v1/users`  
  Принимает JSON, валидирует поля, возвращает JSON с результатом (без сохранения в БД в скелете).
