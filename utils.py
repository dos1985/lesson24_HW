import re
from typing import List,  Union, Iterator, Set

from flask import abort


def lines(filename: str) -> Iterator[str]:
    with open(filename, encoding='utf-8') as file:
        for line in file:
            yield line


def limit(iterable: Union[List, Iterator], value: str) -> Iterator[str]:
    counter: int = 0
    it: Iterator = iter(iterable)
    _value: int = int(value)
    while counter < _value:
        yield next(it)
        counter += 1


def unique(iterable: Union[List, Iterator], *args: List) -> Set:
    return set(iterable)


def xfilter(iterable: Union[List, Iterator], value: str) -> filter:
    return filter(lambda x: value in x, iterable)


def sort(iterable: Union[List, Iterator], value: str) -> Union[List, None]:
    if value == 'asc':
        return sorted(iterable)
    elif value == 'desc':
        return sorted(iterable, reverse=True)
    else:
        abort(400)


def xmap(iterable: Union[List, Iterator], value: str) -> map:
    return map(lambda item: item.split()[int(value)], iterable)


def regex(iterable: Union[List, Iterator], value: str) -> filter:
    filter_obj = filter(lambda x: True if re.search(value, x) else False, iterable)
    return filter_obj