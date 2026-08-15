from collections.abc import Mapping
from typing import Any

import httpx


class HttpClient:
    def __init__(
        self,
        base_url: str,
        headers: Mapping[str, str] | None = None,
        timeout: float = 30,
    ) -> None:
        self._client = httpx.AsyncClient(
            base_url=base_url.rstrip("/"),
            headers=dict(headers or {}),
            timeout=timeout,
        )

    async def get(self, path: str, **kwargs: Any) -> httpx.Response:
        response = await self._client.get(path, **kwargs)
        response.raise_for_status()
        return response

    async def get_json(self, path: str, **kwargs: Any) -> Any:
        response = await self.get(path, **kwargs)
        return response.json()

    async def get_paginated(
        self, path: str, **kwargs: Any
    ) -> list[dict[str, Any]]:
        items: list[dict[str, Any]] = []
        next_url: str | None = path

        while next_url is not None:
            data = await self.get_json(next_url, **kwargs)

            if not isinstance(data, dict) or "results" not in data:
                raise ValueError("Expected paginated response with a results field")

            items.extend(data["results"])
            next_url = data.get("next")

        return items

    async def close(self) -> None:
        await self._client.aclose()
