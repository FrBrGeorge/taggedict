#!/usr/bin/env python3
"""Get taggedict item(s)."""

import sys
import pytest
from taggedict import Tagged


class TestGetitem:
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
        assert set(example["a":]) == {(frozenset("ad"), 2), (frozenset("qwas"), 3)}

    def test_stop(self, example):
        """Tagged[:tags] interface."""
        assert set(example[:"aw"]) == {(frozenset("qwas"), 3)}

    def test_step(self, example):
        """Tagged[::tags] interface."""
        assert set(example[::"ar"]) == {(frozenset("qwer"), 1),
                                        (frozenset("ad"), 2),
                                        (frozenset("qwas"), 3)}

    def test_unknown(self, example):
        """Unimplemented interface."""
        assert example[1:2:3] == NotImplemented
