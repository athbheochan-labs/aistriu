from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import Settings, get_settings
from app.domains.weblate.client import WeblateClient
from app.domains.weblate.manager import WeblateManager
from app.domains.weblate.router import weblate_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = app.state.settings
    if settings.weblate_base_url is None or settings.weblate_api_key is None:
        raise RuntimeError("WEBLATE_BASE_URL and WEBLATE_API_KEY must be set")
    weblate_client = WeblateClient(
        base_url=settings.weblate_base_url,
        token=settings.weblate_api_key,
    )
    app.state.weblate_manager = WeblateManager(client=weblate_client)

    try:
        yield
    finally:
        await weblate_client.close()


def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or get_settings()

    app = FastAPI(title=settings.app_name, debug=settings.debug, lifespan=lifespan)
    app.state.settings = settings

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origin_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router)
    app.include_router(weblate_router)

    return app


app = create_app()
