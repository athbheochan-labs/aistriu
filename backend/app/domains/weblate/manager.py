from typing import Any

from app.domains.weblate.client import WeblateClient
from app.domains.weblate.mapping import map_irish_projects


class WeblateManager:
    def __init__(self, client: WeblateClient) -> None:
        self._client = client

    async def get_language_stats(self) -> dict:
        return await self._client.get_language_stats()

    async def get_projects(self) -> list[dict[str, Any]]:
        return await self._client.get_projects()

    async def list_project_languages(self, project_slug: str) -> list[dict[str, Any]]:
        return await self._client.get_project_languages(project_slug)

    async def get_irish_language_projects_page(
        self, page: int, page_size: int
    ) -> dict[str, Any]:
        projects_page = await self._client.get_projects_page(page, page_size)
        irish_project_matches: list[dict[str, Any]] = []
        errors: list[dict[str, str]] = []

        for project in projects_page["results"]:
            try:
                languages = await self.list_project_languages(project["slug"])
            except Exception as exc:
                errors.append({"project": project["slug"], "error": type(exc).__name__})
                continue

            irish_stats = next(
                (language for language in languages if language["code"] == "ga"),
                None,
            )

            if irish_stats is not None:
                irish_project_matches.append(
                    {
                        "project": project,
                        "irish_stats": irish_stats,
                    }
                )

        return {
            "projects": map_irish_projects(irish_project_matches),
            "page": page,
            "page_size": page_size,
            "total_projects": projects_page["count"],
            "has_next": projects_page["next"] is not None,
            "has_previous": projects_page["previous"] is not None,
            "errors": errors,
        }
