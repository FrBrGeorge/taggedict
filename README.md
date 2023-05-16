Tagged dict
===========

Tags-aware dictionary.

![test](https://github.com/FrBrGeorge/taggedict/actions/workflows/test.yml/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/tagged-dict/badge/?version=latest)](https://tagged-dict.readthedocs.io/en/latest/?badge=latest)

Python `dict` that uses frozenset of tags as actual key, and allows indexing by subset or by individual tag. All standard dict operations inherited from `dict`, but indexing by slice allows some set operations and returns an iterator.

See [technical docimentation](https://tagged-dict.readthedocs.io/en/latest/)
