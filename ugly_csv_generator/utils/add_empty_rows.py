"""Submodule to add random empty rows to a csv file"""

from random import Random
import pandas as pd
import numpy as np
from tqdm.auto import trange
from ugly_csv_generator.utils.add_row import add_row


def add_empty_rows(csv: pd.DataFrame, state: Random, verbose: bool) -> pd.DataFrame:
    """Add random empty rows.

    Parameters
    --------------------------
    csv: pd.DataFrame,
        The DataFrame to add the empty rows to.
    state: Random,
        The random state to use for the generation.
    verbose: bool,
        Whether to show the loading bars.
    """
    rows_number = state.randint(0, max(1, len(csv) // 2))
    empties = np.empty(len(csv.columns))
    empties.fill(np.nan)
    for _ in trange(
        rows_number,
        desc="Adding empty rows",
        disable=not verbose or rows_number <= 1,
        leave=False,
        dynamic_ncols=True,
    ):
        csv = add_row(csv, empties, state=state)
    return csv
