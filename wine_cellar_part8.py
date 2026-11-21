# === Stage 8: Поиск по нескольким словам ===
# Project: WineCellar
def parse_search_query(query):
    tokens = query.lower().split()
    must_have = []
    exclude = []
    for token in tokens:
        if token.startswith('-'):
            exclude.append(token[1:].strip())
        elif token:
            must_have.append(token)
    return must_have, exclude


def normalize_word(word):
    return word.strip().strip('.')


def build_query_regex(must_have, exclude):
    must_parts = []
    for word in must_have:
        normalized = normalize_word(word)
        if not normalized:
            continue
        escaped = re.escape(normalized)
        pattern = '(?:%s)' % escaped
        must_parts.append(pattern)
    if must_parts:
        must_pattern = '(?=%s)' % '|'.join(must_parts)
    else:
        must_pattern = ''
    exclude_parts = []
    for word in exclude:
        normalized = normalize_word(word)
        if not normalized:
            continue
        escaped = re.escape(normalized)
        exclude_parts.append('(?![^\\s%])%s' % escaped)
    exclude_pattern = ''.join(exclude_parts)
    return must_pattern + exclude_pattern


def filter_bottles(bottles, query):
    must_have, exclude = parse_search_query(query)
    regex = build_query_regex(must_have, exclude)
    if not must_have and not exclude:
        return list(bottles)
    result = []
    for bottle in bottles:
        haystack = ' '.join([
            bottle.get('name', ''),
            bottle.get('region', ''),
            str(bottle.get('year', '')),
        ]).lower()
        if regex and not re.search(regex, haystack):
            continue
        result.append(bottle)
    return result


def search_bottles(bottles, query):
    return filter_bottles(bottles, query)


if __name__ == '__main__':
    sample_bottles = [
        {'name': 'Chateau Margaux', 'region': 'Bordeaux', 'year': 2010, 'quantity': 3},
        {'name': 'Opus One', 'region': 'Napa Valley', 'year': 2015, 'quantity': 1},
        {'name': 'Penfolds Grange', 'region': 'South Australia', 'year': 2005, 'quantity': 2},
        {'name': 'Chateau Latour', 'region': 'Bordeaux', 'year': 2001, 'quantity': 5},
        {'name': 'Dom Perignon', 'region': 'Champagne', 'year': 2012, 'quantity': 6},
    ]
    print(search_bottles(sample_bottles, 'bordeaux 2010'))
    print(search_bottles(sample_bottles, 'bordeaux -latour'))
    print(search_bottles(sample_bottles, 'napa -opus'))
    print(search_bottles(sample_bottles, 'champagne'))
    print(search_bottles(sample_bottles, ''))
