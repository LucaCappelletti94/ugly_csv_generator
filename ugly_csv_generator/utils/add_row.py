import pandas as pd
from typing import List
from random import Random


def add_row(csv: pd.DataFrame, values: List, iloc: int = None, state: Random = None):
    if iloc is None:
        iloc = state.randint(0, len(csv))
    return pd.concat([
        csv.iloc[:iloc], 
        pd.DataFrame(dict(zip(csv.columns, values)), index=[iloc]),
        csv.iloc[iloc:]
    ]).reset_index(drop=True)
