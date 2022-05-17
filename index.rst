.. taggedict documentation master file, created by
   sphinx-quickstart on Tue May 17 17:28:26 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root ``toctree`` directive.

Tags-aware dictionary
=====================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   API

Dictionary that uses frozenset of tags as actual key and allows indexing by subset or individual tag. All standard dict operations inherited from ``dict``, but indexing by slice allows some set operations and returns an iterator.

The following indexing conventions are followed:

* When key is a sequence, it first converted to ``frozenset()``, then used as an ordinary dictionary key
* When key is a slice,  with non-empty «start» field (as in ``Dict[key:]``), the resulting operation is performed over the sequence of items tagged 
* When key is a slice, the resulting operation is performed over the sequence of items, i. e. ``key, value`` pairs, tagged by ``key`` tag — that means ``key`` is among ``value`` frozenset.

  * Slice with non-empty «start» part (as in ``Dict[key:]``) generates a sequence of items tagged by ``key`` tag
  * Slice with non-empty «stop» part (as in ``Dict[:keys]``) generates a sequence of items tagged by *all* the files in ``keys`` sequence
  * Slice with non-empty «step» part (as in ``Dict[::keys]``) generates a sequence of items tagged by *any* tag from ``keys`` sequence

Additionally, ``Tagged[slice] = tags`` construction is used for adding tags to values, not to change items themselves.

Examples
========

**TODO**

Indices and tables
==================


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
