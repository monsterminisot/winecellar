# === Stage 6: Генерация идентификаторов ===
# Project: WineCellar
PREFIX = "wcellar"


class IDCollisionError(Exception):
    def __init__(self, prefix, value):
        self.prefix = prefix
        self.value = value
        self.name = f"{prefix}:{value}"
        super().__init__(f"ID collision for {self.name}")


def _is_valid(value):
    if not isinstance(value, str):
        return False
    if len(value) > 100:
        return False
    forbidden = set(" \t\n\r\0")
    return not any(ch in forbidden for ch in value)


def generate_id(prefix, value):
    if not value:
        raise ValueError("value must not be empty")
    if not _is_valid(value):
        raise ValueError(f"invalid id value: {value!r}")
    if not _is_valid(prefix):
        raise ValueError(f"invalid id prefix: {prefix!r}")
    candidate = f"{prefix}:{value}"
    used = IDRegistry._registry
    if candidate in used:
        raise IDCollisionError(prefix, value)
    used.add(candidate)
    return candidate


class IDRegistry:
    _registry = set()

    @classmethod
    def register(cls, prefix, value):
        return generate_id(prefix, value)

    @classmethod
    def is_available(cls, prefix, value):
        candidate = f"{prefix}:{value}"
        return candidate not in cls._registry

    @classmethod
    def clear(cls):
        cls._registry.clear()

    @classmethod
    def list_ids(cls, prefix=None):
        items = cls._registry
        if prefix:
            items = {item for item in items if item.startswith(f"{prefix}:")}
        return sorted(items)
