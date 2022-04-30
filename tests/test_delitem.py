#!/usr/bin/env python3
'''
Delete tagged item/tags.
'''

import pytest
from tagged import Tagged


class TestDelitem:
    """Tagged.__delitem__()."""

    @pytest.fixture
    def example(self):
        """Common tagged dict."""
        return Tagged(wqerr=1, adad=2, qaws=3)

    def test_raw(self, example):
        """No raw key in tagged dict."""
        with pytest.raises(KeyError):
            del example[1]

    def test_seq(self, example):
        """Sequence as a key."""
        del example["addada"]
        assert Tagged(example["a":]) == Tagged(swaq=3)

    def test_start(self, example):
        """del Tagged[tag:] interface."""
        del example["a":]
        assert example == Tagged(rwqe=1, d=2, wqs=3)

    def test_stop(self, example):
        """del Tagged[:tag]  interface."""
        del example[:"aq"]
        assert example == Tagged(rwqe=1, ad=2, ws=3)

    def test_step(self, example):
        """del Tagged[::tag] interface."""
        del example[::"qs"]
        assert example == Tagged(ad=2, wre=1, aw=3)

    def test_estart(self, example):
        """del Tagged[tag:...] interface."""
        del example["a":...]
        assert len(example) == 1

    def test_estop(self, example):
        """del Tagged[...:tag]  interface."""
        del example[...:"aq"]
        assert len(example) == 2

    def test_estep(self, example):
        """del Tagged[...::tag] interface."""
        del example[...::"qs"]
        assert len(example) == 1

    def test_unimpl(self, example):
        """Unimplemented deletion."""
        with pytest.raises(KeyError):
            del example[...:1:1]
