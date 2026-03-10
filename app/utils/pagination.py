from __future__ import annotations

from dataclasses import dataclass
from math import ceil
from typing import Generic, Sequence, TypeVar

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class Page(Generic[T]):
    """A single paginated slice with navigation metadata."""

    items: tuple[T, ...]
    page: int
    per_page: int
    total_items: int
    total_pages: int

    @property
    def has_next(self) -> bool:
        return self.page < self.total_pages

    @property
    def has_previous(self) -> bool:
        return self.page > 1


class PaginationError(ValueError):
    """Raised when pagination parameters are invalid."""


def paginate_sequence(items: Sequence[T], *, page: int, per_page: int) -> Page[T]:
    """Paginate any in-memory sequence into a stable `Page` value object.

    Args:
        items: Full list/tuple of objects.
        page: 1-based page index.
        per_page: Number of items per page.

    Returns:
        A `Page` object with sliced items and metadata.

    Raises:
        PaginationError: if page/per_page are non-positive.
    """

    if page < 1:
        raise PaginationError("page must be >= 1")
    if per_page < 1:
        raise PaginationError("per_page must be >= 1")

    total_items = len(items)
    total_pages = max(1, ceil(total_items / per_page))
    safe_page = min(page, total_pages)

    start = (safe_page - 1) * per_page
    end = start + per_page

    return Page(
        items=tuple(items[start:end]),
        page=safe_page,
        per_page=per_page,
        total_items=total_items,
        total_pages=total_pages,
    )
