import json
from typing import Any

from valkey.asyncio import Valkey


class Cache:
    def __init__(self, url: str) -> None:
        self._client = Valkey.from_url(url, decode_responses=True)

    async def get_json(self, key: str) -> Any | None:
        value = await self._client.get(key)
        if value is None:
            return None
        return json.loads(value)

    async def set_json(self, key: str, value: Any, ttl_seconds: int) -> None:
        await self._client.set(key, json.dumps(value), ex=ttl_seconds)

    async def close(self) -> None:
        await self._client.aclose()
