"""Test the uglify function."""

import random
import os
from random_csv_generator import random_csv
import pandas as pd
from tqdm.auto import trange
from ugly_csv_generator import uglify


def test_uglify():
    """Test the uglify function."""
    state = random.Random(1234567890)
    for i in trange(100, leave=False):
        for include_unicode in [True, False]:
            csv = random_csv(
                number_of_rows=state.randint(1, 100), random_state=(i + 1) * 34567890
            )
            
            for j in trange(3, leave=False):
                csv_inner = csv[csv.columns[(j + 1) * 2 :]]
                ugly1 = uglify(csv_inner, seed=i, satellite_artefacts=True, replace_ones=True, replace_zeros=True, include_unicode=include_unicode)
                ugly2 = uglify(csv_inner, seed=i, satellite_artefacts=True, replace_ones=True, replace_zeros=True, include_unicode=include_unicode)

                pd.testing.assert_frame_equal(ugly1, ugly2)


def test_loading_csv_from_path():
    """Test the loading of a csv from a path."""
    state = random.Random(1234567890)
    for i in trange(100, leave=False):
        for include_unicode in [True, False]:
            csv = random_csv(
                number_of_rows=state.randint(1, 100), random_state=(i + 1) * 34567890
            )

            for j in trange(3, leave=False):
                csv_inner = csv[csv.columns[(j + 1) * 2 :]]
                csv_inner.to_csv("test.csv", index=False)
                ugly1 = uglify("test.csv", seed=i, satellite_artefacts=True, replace_ones=True, replace_zeros=True, include_unicode=include_unicode)
                ugly2 = uglify("test.csv", seed=i, satellite_artefacts=True, replace_ones=True, replace_zeros=True, include_unicode=include_unicode)

                pd.testing.assert_frame_equal(ugly1, ugly2)

    if os.path.exists("test.csv"):
        os.remove("test.csv")
