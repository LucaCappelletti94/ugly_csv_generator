from .add_row import add_row
import pandas as pd
import numpy as np
from random import Random
from tqdm.auto import tqdm


def add_empty_rows(csv: pd.DataFrame, state: Random) -> pd.DataFrame:
    """Add random empty rows"""
    rows_number = state.randint(0, len(csv))
    empties = np.empty(len(csv.columns))
    empties.fill(np.nan)
    for _ in tqdm(range(rows_number), desc="Adding empty rows"):
        csv = add_row(csv, empties, state=state)
    return csv
