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
        Get an object or sequence of objects.

        Raw indexing: convert idx to frozenset and get an object;
        if key is not iterable, act like standard dict.

        Tagged[tag:] — return iterable over items (pairs) tagged by single tag
        Tagged[:tags] — return iterable over items (pairs) tagged by all tags
        Tagged[::tags] — return iterable over items (pairs) tagged by any tag from tags
        """
        match idx:
            case slice(start=start, stop=None, step=None):
                return ((key, val) for key, val in self.items() if start in key)
            case slice(start=None, stop=stop, step=None):
                tags = frozenset(stop)
                return ((key, val) for key, val in self.items() if tags.issubset(key))
            case slice(start=None, stop=None, step=step):
                tags = frozenset(step)
                return ((key, val) for key, val in self.items() if tags & key)
            case slice(start=_, stop=_, step=_):
                return NotImplemented
            case _:
                if seq := iterable(idx):
                    return super().__getitem__(frozenset(seq))
                return super().__getitem__(seq)

    def __setitem__(self, idx, value):
        """
        Update/set an object or object tag(s).

        Raw indexing: convert idx to frozenset if iterable,
        then, act like standard dict.

        Tagged[tag:] = newtags — add (append tags from) newtags to the objects tagged by tag
        Tagged[:tags] = newtags — addppend newtags to the objects tagged by all tags
        Tagged[::tags] = newtags — addpend newtags to the objects tagged by any tag from tags

        If newtags is not iterable, treat it as a single tag sequence
        """
        upd = set(iterable(value) or [value])
        match idx:
            case slice(start=start, stop=None, step=None):
                new = {key | upd: val for key, val in self[idx] if start in key}
                old = [key for key, val in self[idx]]
                for key in old:
                    del self[key]
                self |= new
            case slice(start=None, stop=stop, step=None):
                tags = frozenset(stop)
                new = {key | upd: val for key, val in self[idx] if tags.issubset(key)}
                old = [key for key, val in self[idx]]
                for key in old:
                    del self[key]
                self |= new
            case slice(start=None, stop=None, step=step):
                tags = frozenset(step)
                new = {key | upd: val for key, val in self[idx] if tags & key}
                old = [key for key, val in self[idx]]
                for key in old:
                    del self[key]
                self |= new
            case slice(start=_, stop=_, step=_):
                raise KeyError(f"Complex access via {idx} not implemented")
            case _:
                if seq := iterable(idx):
                    super().__setitem__(frozenset(seq), value)
                else:
                    raise KeyError(f"Iterable key expected, got {idx.__class__}")
