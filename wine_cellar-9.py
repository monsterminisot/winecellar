# === Stage 9: Теги ===
# Project: WineCellar
import re


class Tag:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Tag) and other.name == self.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"Tag({self.name!r})"


_TAG_RE = re.compile(r"^(?:#|@)?([A-Za-z0-9_][A-Za-z0-9_\s\-]{1,40})$")


def parse_tag(token):
    match = _TAG_RE.match(token.strip())
    if not match:
        raise ValueError(f"Недопустимый тег: {token!r}")
    return Tag(match.group(1).strip())


def format_tag(tag):
    return f"#{tag.name}"


class TagManager:
    def __init__(self):
        self._tags = {}

    def add_tag(self, name):
        tag = parse_tag(name)
        if tag not in self._tags:
            self._tags[tag] = tag
        return tag

    def remove_tag(self, name):
        return self._tags.pop(self._tags.get(self._normalize(name)), None)

    def get_tag(self, name):
        return self._tags.get(self._normalize(name))

    def has_tag(self, name):
        return name in self._tags

    def __contains__(self, name):
        return self.has_tag(name)

    def __iter__(self):
        return iter(self._tags.values())

    def __len__(self):
        return len(self._tags)

    def _normalize(self, name):
        if isinstance(name, Tag):
            name = name.name
        return Tag(name.strip())

    def __repr__(self):
        return f"TagManager({list(self._tags)})"
