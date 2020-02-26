import pandas as pd
from typing import List
from random import Random
from .add_chunk import add_chunk


def add_row(csv: pd.DataFrame, values: List, iloc: int = None, state: Random = None):
    if iloc is None:
        iloc = state.randint(0, len(csv))
    return add_chunk(csv, pd.DataFrame(dict(zip(csv.columns, values)), index=[iloc]), iloc)