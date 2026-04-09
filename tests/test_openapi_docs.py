from webtest import TestApp

from app import create_app


def test_openapi_yaml_served() -> None:
    """Эндпоинт /openapi.yaml отдаёт YAML со строкой openapi: 3.0.3."""
    app = create_app()
    client = TestApp(app)
    response = client.get("/openapi.yaml")

    assert response.status_code == 200
    assert "openapi: 3.0.3" in response.text
    assert "text/yaml" in response.headers.get("Content-Type", "")


def test_openapi_json_served() -> None:
    """Эндпоинт /openapi.json отдаёт JSON с корнем openapi."""
    app = create_app()
    client = TestApp(app)
    response = client.get("/openapi.json")

    assert response.status_code == 200
    assert response.json["openapi"] == "3.0.3"


def test_docs_redoc_and_swagger_static() -> None:
    """Страницы /docs и /redoc и статика /swagger-ui/ доступны."""
    app = create_app()
    client = TestApp(app)

    docs = client.get("/docs")
    redoc = client.get("/redoc")
    css = client.get("/swagger-ui/swagger-ui.css")

    assert docs.status_code == 200
    assert "swagger-ui" in docs.text
    assert redoc.status_code == 200
    assert "openapi.yaml" in redoc.text
    assert css.status_code == 200
    assert len(css.body) > 1000
