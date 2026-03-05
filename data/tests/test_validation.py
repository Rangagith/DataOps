import pandas as pd

def test_negative_amount():
    df = pd.read_csv("data/sales.csv")
    assert (df["amount"] >= 0).all(), "Negative amount found!"
