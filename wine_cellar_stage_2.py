# === Stage 2: Проверка полей ===
# Project: WineCellar
import re


WINE_REGIONS = {
    "europa": ["франция", "италия", "испания", "германия", "австрия", "чехия", "венгрия", "греция", "португалия", "россия", "украина", "польша", "болгария", "сербия", "хорватия", "румыния", "hungary", "france", "italy", "spain", "germany", "austria"],
    "america": ["argentina", "chile", "usa", "mexico", "canada", "bolivia", "peru", "ecuador"],
    "asia": ["china", "japan", "thailand", "vietnam", "indonesia", "australia", "new zealand", "south africa"],
}


def normalize_input(value):
    text = value.strip()
    if not text:
        raise ValueError("Введите непустое значение.")
    if not text[0].isalpha():
        raise ValueError("Значение должно начинаться с буквы.")
    return text


def is_valid_region(region):
    normalized = region.strip().lower()
    return normalized in WINE_REGIONS


def validate_name(name):
    normalized = normalize_input(name)
    if len(normalized) < 2:
        raise ValueError("Название должно содержать не менее двух символов.")
    if not all(ch.isprintable() for ch in normalized):
        raise ValueError("Название не может содержать управляющие символы.")
    return normalized


def validate_region(region):
    normalized = normalize_input(region)
    if not is_valid_region(normalized):
        raise ValueError(f"Неизвестный регион '{region}'. Поддерживаемые: {sorted(WINE_REGIONS)}.")
    return normalized


def validate_year(year):
    year = normalize_input(year)
    year = re.sub(r"[^0-9]", "", year)
    if not year:
        raise ValueError("Год должен состоять только из цифр.")
    year = int(year)
    if year < 1800 or year > datetime.now().year + 5:
        raise ValueError(f"Год должен быть в диапазоне от 1800 до {datetime.now().year + 5}.")
    return year


def validate_quantity(quantity):
    quantity = normalize_input(quantity)
    quantity = re.sub(r"[^0-9]", "", quantity)
    if not quantity:
        raise ValueError("Количество должно быть положительным целым числом.")
    quantity = int(quantity)
    if quantity <= 0:
        raise ValueError("Количество не может быть меньше или равно нулю.")
    if quantity > 999:
        raise ValueError("Максимальное количество в одной бутылке — 999.")
    return quantity
