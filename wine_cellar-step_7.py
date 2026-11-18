# === Stage 7: Сортировка записей ===
# Project: WineCellar
from datetime import datetime


def _create_sort_key(item):
    created_at = item.get("created_at")
    created_at = datetime.fromisoformat(created_at) if created_at else datetime.max
    return created_at.isoformat(), item.get("name", "")


def sort_by_name(items, ascending=True):
    return sorted(items, key=lambda i: i.get("name", "").lower(),
                  reverse=not ascending)


def sort_by_creation(items, ascending=True):
    return sorted(items, key=_create_sort_key, reverse=not ascending)


def sort_bottles(items, field="name", ascending=True):
    if field == "name":
        return sort_by_name(items, ascending)
    if field == "created_at":
        return sort_by_creation(items, ascending)
    return sorted(items, key=lambda i: i.get(field), reverse=not ascending)
