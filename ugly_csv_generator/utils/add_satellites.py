"""Submodule to add satellites to a CSV file

A satellite is a small table-like artefact that is added randomly around the CSV
to simulate the presence of random scribbling around the data. While it really should
not exist in well-formed CSV files, it is sadly common in the real world.

A memorable example of a satellite, is when some data-entry person wrote the
order of pizzas for a party on the same sheet as the financial report.
"""

import os
from random import Random
from glob import glob
import pandas as pd
from ugly_csv_generator.utils.add_chunk import add_chunk


def random_satellite(state: Random):
    """Pick a random satellite from the available ones.

    Parameters
    --------------------------
    state: Random,
        The random state to use for the generation.
    """
    satellites = glob(f"{os.path.dirname(os.path.abspath(__file__))}/satellites/*.csv")
    return pd.read_csv(state.choice(satellites), header=None)


def add_satellites(csv: pd.DataFrame, state: Random) -> pd.DataFrame:
    """Add satellites to the provided DataFrame.

    Parameters
    --------------------------
    csv: pd.DataFrame,
        The DataFrame to add the satellites to.
    state: Random,
        The random state to use for the generation.
    """
    if state.randint(0, 1) == 1:
        csv = add_chunk(csv, random_satellite(state), 0)
    if state.randint(0, 1) == 1:
        csv = add_chunk(csv, random_satellite(state), len(csv))
    return csv
