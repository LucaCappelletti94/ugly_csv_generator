import pandas as pd
import numpy as np
from random import Random
from tqdm.auto import tqdm


def add_empty_columns(csv: pd.DataFrame, state: Random, verbose: bool) -> pd.DataFrame:
    """Add random empty columns"""
    columns_number = state.randint(0, len(csv.columns))
    for number in tqdm(range(columns_number), desc="Adding empty columns", disable=not verbose or columns_number==0):
        loc = state.randint(0, len(csv.columns))
        csv.insert(
            loc=loc,
            column="{column}{separator}{number}".format(
                column=state.choice(csv.columns),
                separator=state.choice(("", " ", ".", "_", "-")),
                number=number
            ),
            value=np.nan
        )
    return csv
