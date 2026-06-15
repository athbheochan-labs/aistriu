import asyncio

from app.api.routes.health import health_check
from app.main import create_app


def test_health_check_returns_ok() -> None:
    assert asyncio.run(health_check()) == {"status": "ok"}


def test_create_app_registers_health_route() -> None:
    app = create_app()

    assert any(route.path == "/health" for route in app.routes)
