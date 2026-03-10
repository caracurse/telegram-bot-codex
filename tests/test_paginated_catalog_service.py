import asyncio
from unittest.mock import AsyncMock

from app.services.paginated_catalog_service import CatalogItem, PaginatedCatalogService


def test_get_page_uses_repository_and_paginates() -> None:
    repository = AsyncMock()
    repository.list_for_user.return_value = [
        CatalogItem(id=1, title="One", description="First"),
        CatalogItem(id=2, title="Two", description="Second"),
        CatalogItem(id=3, title="Three", description="Third"),
    ]

    service = PaginatedCatalogService(repository=repository)

    page = asyncio.run(service.get_page(user_id=42, page=2, per_page=2))

    repository.list_for_user.assert_awaited_once_with(42)
    assert [item.id for item in page.items] == [3]
    assert page.page == 2
    assert page.total_pages == 2
