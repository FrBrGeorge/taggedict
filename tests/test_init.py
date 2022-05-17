#!/usr/bin/env python3
"""Create a tagged dict."""

import sys
import pytest
from taggedict import Tagged


class TestInit:
    """Tagged.__init__()."""

    def test_exact(self):
        """Init by frozenset."""
        t = Tagged({frozenset({10, 20, 30}): 1, frozenset({4, 5, 6}): 2})
        assert 1 in t.values()
        assert frozenset({10, 20, 30}) in t.keys()

    def test_seq(self):
        """Init by some sequences."""
        t = Tagged({(10, 20, 30): 1, (4, 5, 6): 2})
        assert 1 in t.values()
        assert frozenset({10, 20, 30}) in t.keys()

    def test_pairs(self):
        """Init by sequence of pairs."""
        t = Tagged({("qwerqwer", 1), ("aasdf", 2)})
        assert 2 in t.values()
        assert frozenset("qwer") in t.keys()

    def test_kwargs(self):
        """Init by kwargs."""
        t = Tagged(qwerqwer=1, bzzzz=2)
        assert 1 in t.values()
        assert frozenset("bz") in t.keys()

    def test_empty(self):
        """Non-tagged init."""
        t = Tagged()
        assert len(list(t.items())) == 0
