from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from app.utils.pagination import Page, paginate_sequence


@dataclass(frozen=True, slots=True)
class CatalogItem:
    id: int
    title: str
    description: str


class CatalogRepository(Protocol):
    async def list_for_user(self, user_id: int) -> list[CatalogItem]:
        """Return all available entities for the user."""


class PaginatedCatalogService:
    """Shared pagination orchestrator for shop, inventory and quest lists.

    Handlers can use this service to stay thin while pagination logic remains
    centralized and testable.
    """

    def __init__(self, repository: CatalogRepository) -> None:
        self._repository = repository

    async def get_page(
        self,
        *,
        user_id: int,
        page: int,
        per_page: int,
    ) -> Page[CatalogItem]:
        entries = await self._repository.list_for_user(user_id)
        return paginate_sequence(entries, page=page, per_page=per_page)
