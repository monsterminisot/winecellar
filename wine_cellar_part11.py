# === Stage 11: Постраничный вывод ===
# Project: WineCellar
page_size = 12


def page_data(items, page, page_size):
    if page < 1:
        page = 1
    if page_size < 1:
        page_size = 1
    start = (page - 1) * page_size
    return items[start:start + page_size]


def total_pages(count, page_size):
    if count == 0:
        return 1 if page_size > 0 else 0
    return max(1, (count + page_size - 1) // page_size)


def bottle_page(bottles, page, page_size):
    total = len(bottles)
    total_pages_count = total_pages(total, page_size)
    if page < 1:
        page = 1
    if page > total_pages_count:
        page = total_pages_count
    sliced = page_data(bottles, page, page_size)
    return {
        "items": sliced,
        "page": page,
        "page_size": page_size,
        "total": total,
        "total_pages": total_pages_count,
        "has_prev": page > 1,
        "has_next": page < total_pages_count,
    }
