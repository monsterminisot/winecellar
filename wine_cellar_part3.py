# === Stage 3: Хранилище в памяти ===
# Project: WineCellar
wine_store.py

from typing import List, Optional


class Bottle:
    """Сущность «бутылка» в домашнем погребе WineCellar."""

    def __init__(self, name: str, region: str, year: int, quantity: int) -> None:
        self.name = name
        self.region = region
        self.year = year
        self.quantity = quantity

    def __repr__(self) -> str:
        return (
            f"Bottle(name={self.name!r}, region={self.region!r}, "
            f"year={self.year}, quantity={self.quantity})"
        )


class BottleStore:
    """Хранилище бутылок в памяти: добавление, получение по id и список."""

    def __init__(self) -> None:
        self._store: dict[str, Bottle] = {}
        self._counter = 0

    def add(self, bottle: Bottle) -> str:
        """Добавить бутылку и вернуть её идентификатор."""
        self._counter += 1
        bottle_id = str(self._counter)
        self._store[bottle_id] = bottle
        return bottle_id

    def get(self, bottle_id: str) -> Optional[Bottle]:
        """Вернуть бутылку по идентификатору или None, если её нет."""
        return self._store.get(bottle_id)

    def list_bottles(self) -> List[Bottle]:
        """Вернуть список всех бутылок в порядке добавления."""
        return list(self._store.values())

    def __len__(self) -> int:
        return len(self._store)
