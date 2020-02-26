from ugly_csv_generator import uglify
from random_csv_generator import random_csv
import pandas as pd


def test_uglify():
    for _ in range(3):
        csv = random_csv()
        ugly1 = uglify(csv)
        ugly2 = uglify(csv)

        pd.testing.assert_frame_equal(ugly1, ugly2)
