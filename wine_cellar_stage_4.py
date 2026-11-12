# === Stage 4: Редактирование записей ===
# Project: WineCellar
from typing import List, Optional, Tuple


WINE_FIELDS: Tuple[str, ...] = ("name", "region", "year", "quantity")


class Bottle:
    def __init__(self, name: str, region: str, year: int, quantity: int) -> None:
        self.name = name
        self.region = region
        self.year = year
        self.quantity = quantity

    def to_dict(self) -> dict:
        return {"name": self.name, "region": self.region, "year": self.year, "quantity": self.quantity}


def validate_update_data(data: dict) -> Tuple[dict, List[str]]:
    errors: List[str] = []
    allowed: set[str] = set(WINE_FIELDS)
    filtered: dict[str, object] = {}

    for key, value in data.items():
        if key not in allowed:
            errors.append(f"Поле '{key}' не может быть изменено")
            continue
        if key == "name" and not isinstance(value, str):
            errors.append(f"Поле 'name' должно быть строкой")
        elif key == "region" and not isinstance(value, str):
            errors.append(f"Поле 'region' должно быть строкой")
        elif key == "year" and (not isinstance(value, int) or isinstance(value, bool)):
            errors.append(f"Поле 'year' должно быть целым числом")
        elif key == "quantity" and (not isinstance(value, int) or isinstance(value, bool)):
            errors.append(f"Поле 'quantity' должно быть целым числом")
        else:
            filtered[key] = value

    return filtered, errors


def apply_update(bottle: Bottle, data: dict) -> Tuple[Bottle, List[str]]:
    updated, errors = validate_update_data(data)
    if errors:
        return bottle, errors

    for field in WINE_FIELDS:
        if field in updated:
            setattr(bottle, field, updated[field])

    return bottle, errors


def build_updated_bottle(bottle: Bottle, data: dict) -> Tuple[Optional[Bottle], List[str]]:
    updated, errors = validate_update_data(data)
    if errors:
        return None, errors

    new_bottle = Bottle(
        name=updated.get("name", bottle.name),
        region=updated.get("region", bottle.region),
        year=updated.get("year", bottle.year),
        quantity=updated.get("quantity", bottle.quantity),
    )
    return new_bottle, errors
