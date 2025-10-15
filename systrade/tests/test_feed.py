from datetime import date
from pathlib import Path

import pytest

from systrade.data import BarData
from systrade.feed import FileFeed


def test_is_running():
    """Test is_running indicators"""
    feed = FileFeed(Path(__file__).parent / "bars.csv")
    assert not feed.is_running()
    feed.start()
    assert feed.is_running()
    feed.stop()
    assert not feed.is_running()


def test_subscribe_if_no_symbol_throws():
    """Test subscription will raise exception if no data"""
    feed = FileFeed(Path(__file__).parent / "bars.csv")
    feed.start()

    with pytest.raises(ValueError):
        feed.subscribe("MSFT")


def test_next_data_empty_sub():
    """Test next_data returns nothing if not subscribed"""
    feed = FileFeed(Path(__file__).parent / "bars.csv")
    feed.start()

    assert not feed.next_data()


def test_next_data_after_sub():
    """Test next_data returns nothing if not subscribed"""
    feed = FileFeed(Path(__file__).parent / "bars.csv")
    feed.start()
    feed.subscribe("NVDA")

    assert feed.next_data()


def test_start_with_date_filter():
    feed = FileFeed(
        Path(__file__).parent / "bars.csv", start="2005-02-04", end="2005-02-08"
    )
    feed.start()
    feed.subscribe("NVDA")

    assert feed.is_running()
    d1 = feed.next_data()
    d2 = feed.next_data()
    d3 = feed.next_data()
    assert not feed.is_running()
    assert d1.as_of.date() == date.fromisoformat("2005-02-04")
    assert d2.as_of.date() == date.fromisoformat("2005-02-07")
    assert d3.as_of.date() == date.fromisoformat("2005-02-08")
