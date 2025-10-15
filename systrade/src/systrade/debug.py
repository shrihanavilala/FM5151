from datetime import datetime as dt
from datetime import timedelta, timezone
import pandas as pd
from pathlib import Path
from feed import FileFeed
data = pd.read_csv(Path(__file__).parent.parent.parent / "tests/bars.csv")


data["Date"] = pd.to_datetime(data["Date"])

current = dt.strptime("2005-02-04", "%Y-%m-%d")
end = dt.strptime("2005-02-08", "%Y-%m-%d")
for each in range(3):
    print(current, end)
    mask = data["Date"].apply(dt.date) == current.date()
    pos = mask.idxmax()
    int_loc = data.index.get_loc(pos)
    current = data.iloc[int_loc + 1]["Date"]
            
            
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