#!/usr/bin/env python3
"""Get tagged item(s)."""

import sys
import pytest
from tagged import Tagged


class TestInit:
    """Tagged.__getitem__()."""

    @pytest.fixture
    def example(self):
        """Common tagged dict."""
        return Tagged(wqerr=1, adad=2, qaws=3)

    def test_raw(self, example):
        """No raw key in tagged dict."""
        with pytest.raises(KeyError):
            example[1]

    def test_seq(self, example):
        """Common sequence as key."""
        assert example["ad"] == 2

    def test_start(self, example):
        """Tagged[tag:] interface."""
        assert set(example["a":]) == {2, 3}
