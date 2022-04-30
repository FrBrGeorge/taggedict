#!/usr/bin/env python3
"""
Tagged dict
"""
_F = frozenset


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
            super().__init__({_F(key): val for key, val in args[0].items()})
        elif args:
            super().__init__({_F(key): val for key, val in args[0]})
        elif kwargs:
            super().__init__({_F(key): val for key, val in kwargs.items()})
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
                tags = _F(stop)
                return ((key, val) for key, val in self.items() if tags.issubset(key))
            case slice(start=None, stop=None, step=step):
                tags = _F(step)
                return ((key, val) for key, val in self.items() if tags & key)
            case slice(start=_, stop=_, step=_):
                return NotImplemented
            case _:
                if seq := iterable(idx):
                    return super().__getitem__(_F(seq))
                return super().__getitem__(seq)

    def _moditem(self, idx, upd, tags, setop, mode):
        """
        (internal) Modify tags with setop selecting items by mode
        """
        new = {setop(key, upd): val for key, val in self[idx] if mode(key, tags)} if mode else {}
        old = [key for key, val in self[idx]]
        for key in old:
            del self[key]
        self |= new

    def __delitem__(self, idx):
        """
        Delete object(s) or tag(s).

        Raw indexing: convert idx to frozenset and delete an object;
        if key is not iterable, act like standard dict.

        del Tagged[tag:] — delete tag from all objects tagged by tag
        del Tagged[:tags] — delete tags from all objects tagged by all tags
        del Tagged[::tags] — delete tags from objects tagged by any tag from tags

        del Tagged[tag:...] — delete objects tagged by tag
        del Tagged[...:tags] — delete objects tagged by all tags
        del Tagged[...::tags] — delete objects tagged by any tag from tags
        del Tagged[:...:tags] — same
        """
        if type(idx) is slice:
            idx = slice(idx.start if idx.start is not Ellipsis else False,
                        idx.stop if idx.stop is not Ellipsis else False,
                        idx.step if idx.step is not Ellipsis else False)
        match idx:
            case slice(start=start, stop=None, step=None):
                self._moditem(idx, {start}, start, _F.__sub__, _F.__contains__)
            case slice(start=None, stop=stop, step=None):
                self._moditem(idx, _F(stop), _F(stop), _F.__sub__, _F.issuperset)
            case slice(start=None, stop=None, step=step):
                self._moditem(idx, _F(step), _F(step), _F.__sub__, _F.__and__)
            case slice(start=start, stop=(None | False), step=(None | False)):
                self._moditem(slice(start, None, None), {start}, _F(start), _F.__sub__, None)
            case slice(start=(None | False), stop=stop, step=(None | False)):
                self._moditem(slice(None, stop, None), _F(stop), _F(stop), _F.__sub__, None)
            case slice(start=(None | False), stop=(None | False), step=step):
                self._moditem(slice(None, None, step), _F(step), _F(step), _F.__sub__, None)
            case slice(start=_, stop=_, step=_):
                raise KeyError(f"Complex access via {idx} not implemented")
            case _:
                if seq := iterable(idx):
                    super().__delitem__(_F(seq))
                else:
                    super().__delitem__(idx)

    def __setitem__(self, idx, value):
        """
        Update/set an object or object tag(s).

        Raw indexing: convert idx to frozenset if iterable,
        then act like standard dict.

        Tagged[tag:] = newtags — add (append tags from) newtags to the objects tagged by tag
        Tagged[:tags] = newtags — addppend newtags to the objects tagged by all tags
        Tagged[::tags] = newtags — addpend newtags to the objects tagged by any tag from tags

        If newtags is not iterable, treat it as a single tag sequence
        """
        upd = set(iterable(value) or [value])
        match idx:
            case slice(start=start, stop=None, step=None):
                self._moditem(idx, upd, start, _F.__or__, _F.__contains__)
            case slice(start=None, stop=stop, step=None):
                self._moditem(idx, upd, _F(stop), _F.__or__, _F.issuperset)
            case slice(start=None, stop=None, step=step):
                self._moditem(idx, upd, _F(step), _F.__or__, _F.__and__)
            case slice(start=_, stop=_, step=_):
                raise KeyError(f"Complex access via {idx} not implemented")
            case _:
                if seq := iterable(idx):
                    super().__setitem__(_F(seq), value)
                else:
                    raise KeyError(f"Iterable key expected, got {idx.__class__}")
