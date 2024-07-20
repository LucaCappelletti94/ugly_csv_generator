"""Submodule to add NaN-like artefacts to a csv file."""

from random import Random
import pandas as pd
import numpy as np


def random_nan(state: Random):
    """Generate a random NaN-like artefact.

    Parameters
    --------------------------
    state: Random,
        The random state to use for the generation.
    """
    if state.randint(0, 1) == 1:
        return state.choice([np.nan, 0, "#RIF!"])
    n = state.randint(1, 10)
    return state.choice([".", "-", "_", "/", " ", "\n", "\n\r"]) * n


def add_nan_like_artefacts(csv: pd.DataFrame, state: Random) -> pd.DataFrame:
    """Add NaN-like artefacts to the provided DataFrame.

    Parameters
    --------------------------
    csv: pd.DataFrame,
        The DataFrame to add the NaN-like artefacts to.
    state: Random,
        The random state to use for the generation.
    """
    return csv.applymap(lambda x: random_nan(state) if pd.isna(x) else x)
