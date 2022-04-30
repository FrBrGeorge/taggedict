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
