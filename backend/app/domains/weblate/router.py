from typing import Any

from fastapi import APIRouter, Query

from app.domains.weblate.dependencies import WeblateManagerDep

weblate_router = APIRouter(prefix="/weblate", tags=["weblate"])


@weblate_router.get("", include_in_schema=False)
@weblate_router.get("/")
async def weblate(manager: WeblateManagerDep) -> dict[str, Any]:
    return await manager.get_language_stats()


@weblate_router.get("/irish-projects")
async def irish_language_projects(
    manager: WeblateManagerDep,
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=25, ge=1, le=100),
) -> dict[str, Any]:
    return await manager.get_irish_language_projects_page(
        page=page, page_size=page_size
    )
