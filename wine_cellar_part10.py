# === Stage 10: Группировка ===
# Project: WineCellar
from collections import Counter


def bottles_by_region(bottles):
    grouped = {}
    for bottle in bottles:
        region = bottle.region
        grouped.setdefault(region, []).append(bottle)
    return grouped


def region_counts(bottles):
    return Counter(bottle.region for bottle in bottles)


def region_totals(bottles):
    totals = {}
    for bottle in bottles:
        totals[bottle.region] = totals.get(bottle.region, 0) + bottle.quantity
    return totals


def top_regions(bottles, limit=5):
    ordered = region_counts(bottles).most_common(limit)
    return [(region, count) for region, count in ordered]


def region_breakdown(bottles):
    totals = region_totals(bottles)
    counts = region_counts(bottles)
    return {
        region: {
            "count": counts.get(region, 0),
            "quantity": totals.get(region, 0),
        }
        for region in totals
    }


def print_region_report(bottles):
    totals = region_totals(bottles)
    print("Регион | Бутылок | Кол-во")
    print("-" * 20)
    for region in sorted(totals, key=lambda r: totals[r], reverse=True):
        print(f"{region:<10} | {totals[region]:<6} | {totals[region]}")


if __name__ == "__main__":
    sample = [
        {"name": "Chateau Margaux", "region": "Bordeaux", "year": 2010, "quantity": 2},
        {"name": "Opus One", "region": "Napa Valley", "year": 2015, "quantity": 1},
        {"name": "Barolo Riserva", "region": "Piedmont", "year": 2016, "quantity": 3},
        {"name": "Chateau Margaux", "region": "Bordeaux", "year": 2011, "quantity": 1},
        {"name": "Opus One", "region": "Napa Valley", "year": 2018, "quantity": 2},
        {"name": "Barolo Riserva", "region": "Piedmont", "year": 2017, "quantity": 1},
    ]
    print_region_report(sample)
    print("\nТоп регионов:")
    for region, count in top_regions(sample):
        print(f"  {region}: {count} бутылок")
