from ugly_csv_generator import uglify
from random_csv_generator import random_csv
import pandas as pd


def test_uglify():
    for i in range(10):
        csv = random_csv()
        ugly1 = uglify(csv, seed=i)
        ugly2 = uglify(csv, seed=i)

        pd.testing.assert_frame_equal(ugly1, ugly2)
