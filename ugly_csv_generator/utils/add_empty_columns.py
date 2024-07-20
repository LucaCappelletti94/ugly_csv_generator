"""Submodule providing an utility to add random empty columns to a CSV."""

from random import Random
import pandas as pd
import numpy as np
from tqdm.auto import trange


def add_empty_columns(csv: pd.DataFrame, state: Random, verbose: bool) -> pd.DataFrame:
    """Add random empty columns to the provided DataFrame.

    Parameters
    --------------------------
    csv: pd.DataFrame,
        The DataFrame to add the empty columns to.
    state: Random,
        The random state to use for the generation.
    verbose: bool,
        Whether to show the loading bars.
    """
    columns_number = state.randint(0, len(csv.columns))
    for number in trange(
        columns_number,
        desc="Adding empty columns",
        disable=not verbose or columns_number <= 1,
        leave=False,
        dynamic_ncols=True,
    ):
        loc = state.randint(0, len(csv.columns))
        column = (state.choice(csv.columns),)
        separator = (state.choice(("", " ", ".", "_", "-")),)
        number = (number,)
        csv.insert(
            loc=loc,
            column=f"{column}{separator}{number}",
            value=np.nan,
        )
    return csv
