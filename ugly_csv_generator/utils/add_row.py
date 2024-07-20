"""Submodule for adding a row to a DataFrame."""

from typing import List
from random import Random
import pandas as pd
from ugly_csv_generator.utils.add_chunk import add_chunk


def add_row(csv: pd.DataFrame, values: List, iloc: int = None, state: Random = None):
    """Add a row to a DataFrame.

    Parameters
    --------------------------
    csv: pd.DataFrame,
        The DataFrame to add the row to.
    values: List,
        The values to add.
    iloc: int = None,
        The index location where to add the row.
    state: Random = None,
        The random state to use for the generation.
    """
    if iloc is None:
        iloc = state.randint(0, len(csv))
    return add_chunk(
        csv, pd.DataFrame(dict(zip(csv.columns, values)), index=[iloc]), iloc
    )
