# === Stage 1: Каркас модуля ===
# Project: WineCellar
from dataclasses import dataclass, field
from typing import List


@dataclass
class Bottle:
    name: str
    region: str
    year: int
    quantity: int
    tastings: List[str] = field(default_factory=list)


def create_demo_records() -> List[Bottle]:
    return [
        Bottle("Chateau Margaux", "Бордо", 2015, 2),
        Bottle("Opus One", "Напа", 2018, 1),
        Bottle("Barolo Riserva", "Пьемонт", 2016, 3),
        Bottle("Chablis 1er Cru", "Бургундия", 2019, 1),
    ]


def main() -> None:
    bottles = create_demo_records()
    print("Добро пожаловать в WineCellar!")
    print(f"В погребе хранится {len(bottles)} бутылок:")
    for bottle in bottles:
        print(f"  {bottle.name} ({bottle.region}, {bottle.year}) - {bottle.quantity} шт.")
