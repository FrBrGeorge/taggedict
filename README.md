Tagged dict
===========

Tags-aware dictionary.

[![Python 3.12](https://github.com/FrBrGeorge/taggedict/actions/workflows/test.yml/badge.svg)](https://github.com/FrBrGeorge/taggedict/actions/workflows/test.yml)
[![Documentation Status](https://readthedocs.org/projects/taggedict/badge/?version=latest)](https://taggedict.readthedocs.io/en/latest/?badge=latest)

Python `dict` that uses frozenset of tags as actual key, and allows indexing by subset or by individual tag. All standard dict operations inherited from `dict`, but indexing by slice allows some set operations and returns an iterator.

See [technical docimentation](https://taggedict.readthedocs.io/en/latest/)
