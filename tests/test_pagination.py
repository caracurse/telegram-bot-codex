import pytest

from app.utils.pagination import PaginationError, paginate_sequence


def test_paginate_sequence_returns_slice_with_meta() -> None:
    data = [1, 2, 3, 4, 5]

    page = paginate_sequence(data, page=2, per_page=2)

    assert page.items == (3, 4)
    assert page.page == 2
    assert page.total_pages == 3
    assert page.total_items == 5
    assert page.has_previous is True
    assert page.has_next is True


def test_paginate_sequence_caps_page_at_last_page() -> None:
    data = [1, 2, 3]

    page = paginate_sequence(data, page=99, per_page=2)

    assert page.page == 2
    assert page.items == (3,)


@pytest.mark.parametrize(
    ("page", "per_page"),
    [
        (0, 10),
        (1, 0),
    ],
)
def test_paginate_sequence_validates_params(page: int, per_page: int) -> None:
    with pytest.raises(PaginationError):
        paginate_sequence([1], page=page, per_page=per_page)
