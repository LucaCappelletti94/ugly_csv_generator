"""This module contains the function to duplicate the schema into random new rows."""

from random import Random
import pandas as pd
from tqdm.auto import trange
from ugly_csv_generator.utils.add_row import add_row


def add_duplicate_schema(
    csv: pd.DataFrame, state: Random, verbose: bool
) -> pd.DataFrame:
    """Duplicate the schema into random new rows.

    Parameters
    --------------------------
    csv: pd.DataFrame,
        The DataFrame to add the duplicated schema to.
    state: Random,
        The random state to use for the generation.
    verbose: bool,
        Whether to show the loading bars.
    """
    schema_number = state.randint(0, max(1, len(csv) // 2))
    for _ in trange(
        schema_number,
        desc="Adding duplicated schemas",
        disable=not verbose or schema_number <= 1,
        leave=False,
        dynamic_ncols=True,
    ):
        csv = add_row(csv, csv.columns, state=state)
    return csv
