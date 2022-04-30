#!/usr/bin/env python3
"""Common tagged abilities."""

import sys
import pytest
from tagged import Tagged


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
