#!/usr/bin/env python3
'''
Set taggedict item/tags.
'''

import pytest
from taggedict import Tagged


class TestSetitem:
    """Tagged.__setitem__()."""

    @pytest.fixture
    def example(self):
        """Common tagged dict."""
        return Tagged(wqerr=1, adad=2, qaws=3)

    def test_raw(self, example):
        """No raw key in tagged dict."""
        with pytest.raises(KeyError):
            example[1] = 2

    def test_seq(self, example):
        """Sequence as a key."""
        example["addada"] = 42
        assert example["ada"] == 42
        assert set(example[:"ada"]) == {(frozenset("ad"), 42)}

    def test_start(self, example):
        """Tagged[tag:] = value interface."""
        example["a":] = "i"
        assert set(example["i":]) == set(example["a":])

    def test_stop(self, example):
        """Tagged[:tag] = value interface."""
        example[:"aq"] = "i"
        assert example["siwaq"] == 3
        assert len(set(example["i":])) == 1

    def test_step(self, example):
        """Tagged[::tag] = value interface."""
        example[::"aw"] = "i"
        assert example["siwaq"] == 3
        assert len(set(example["i":])) == 3

    def test_unimpl(self, example):
        """Unimplemented setitem."""
        with pytest.raises(KeyError):
            example[1:1:1] = 1
