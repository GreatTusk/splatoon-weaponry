from typing import AsyncGenerator, Any

from httpx import AsyncClient


async def get_http_client() -> AsyncGenerator[AsyncClient, Any]:
    async with AsyncClient() as client:
        yield client
