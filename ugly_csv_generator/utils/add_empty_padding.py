import pandas as pd
import numpy as np
from random import Random
from .add_row import add_row


def add_empty_padding(csv: pd.DataFrame, state: Random) -> pd.DataFrame:
    csv = add_row(csv, csv.columns, 0)
    w = len(csv.columns)
    h = len(csv)
    columns_number = state.randint(w, w*2)
    rows_number = state.randint(h, h*2)
    empties = np.empty((rows_number, columns_number), dtype='O')
    empties.fill(np.nan)
    if columns_number-w != 0:
        start_x = state.randint(0, columns_number-w)
    else:
        start_x = 0
    if rows_number-h != 0:
        start_y = state.randint(0, rows_number-h)
    else:
        start_y = 0

    empties[start_y:start_y+h, start_x:start_x+w] = csv.values

    return pd.DataFrame(
        empties, columns=list(range(empties.shape[1]))
    )
