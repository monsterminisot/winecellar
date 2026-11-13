# === Stage 5: Связанная сущность ===
# Project: WineCellar
wine_tasting.py

from datetime import date


class Tasting:
    """Дегустация одной бутылки: когда, как и что понравилось."""

    def __init__(self, bottle_id, notes, rating, tasting_date,
                 aroma="", taste="", aftertaste=""):
        self.bottle_id = bottle_id
        self.notes = notes
        self.rating = rating
        self.tasting_date = tasting_date
        self.aroma = aroma
        self.taste = taste
        self.aftertaste = aftertaste

    def __repr__(self):
        return (f"Tasting(bottle_id={self.bottle_id}, "
                f"rating={self.rating}, date={self.tasting_date})")


class TastingRepository:
    """Хранилище дегустаций в памяти."""

    def __init__(self):
        self._recordings = []

    def add_tasting(self, bottle_id, notes, rating, tasting_date,
                    aroma="", taste="", aftertaste=""):
        tasting = Tasting(
            bottle_id=bottle_id,
            notes=notes,
            rating=rating,
            tasting_date=tasting_date,
            aroma=aroma,
            taste=taste,
            aftertaste=aftertaste,
        )
        self._recordings.append(tasting)
        return tasting

    def get_tastings(self, bottle_id):
        return [t for t in self._recordings if t.bottle_id == bottle_id]

    def all_tastings(self):
        return list(self._recordings)
