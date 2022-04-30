#!/usr/bin/env python3
"""
Tagged dict
"""


def iterable(obj):
    """
    Check if object is iterable.

    Taken from documentation:
    https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable

    :param obj: Object to check
    :return: Iterator over object, False if object is not iterable
    """
    try:
        return iter(obj)
    except TypeError:
        return False


class Tagged(dict):
    """
    Initialize taddeg dictionary.

    Any sequenct ant be provided as key — it will be converted to frozenset
    """

    def __init__(self, *args, **kwargs):
        if args and hasattr(args[0], "items"):
            super().__init__({frozenset(key): val for key, val in args[0].items()})
        elif args:
            super().__init__({frozenset(key): val for key, val in args[0]})
        elif kwargs:
            super().__init__({frozenset(key): val for key, val in kwargs.items()})
        else:
            super().__init__()

    def __getitem__(self, idx):
        """
        Get an item or sequence of items.

        Raw indexing: convert key to frozenset and get an item;
        if key is not iterable, act like standard dict.

        TODO
        """
        match idx:
            case slice(start=start, stop=None, step=None):
                return (val for key, val in self.items() if start in key)
            case _:
                if seq := iterable(idx):
                    return super().__getitem__(frozenset(seq))
                return super().__getitem__(seq)
