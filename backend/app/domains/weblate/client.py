from typing import Any

from app.core.http_client import HttpClient


class WeblateClient(HttpClient):
    def __init__(self, base_url: str, token: str) -> None:
        super().__init__(
            base_url=self._api_base_url(base_url),
            headers={"Authorization": f"Token {token}"},
            timeout=30,
        )

    @staticmethod
    def _api_base_url(base_url: str) -> str:
        base_url = base_url.rstrip("/")
        if base_url.endswith("/api"):
            return base_url
        return f"{base_url}/api"

    async def get_language_stats(self) -> dict:
        return await self.get_json("/languages/ga/statistics/")

    async def get_projects(self) -> list[dict[str, Any]]:
        return await self.get_paginated("/projects/", params={"page_size": 100})

    async def get_project_languages(self, project_slug: str) -> list[dict[str, Any]]:
        languages = await self.get_json(f"/projects/{project_slug}/languages/")

        if not isinstance(languages, list):
            raise ValueError("Expected project languages response to be a list")

        return languages

    async def get_projects_page(self, page: int, page_size: int) -> dict[str, Any]:
        return await self.get_json(
            "/projects/", params={"page": page, "page_size": page_size}
        )
