import pandas as pd
import numpy as np
from random import Random


def random_nan(state: Random):
    if state.randint(0, 1) == 1:
        return state.choice([np.nan, 0, "#RIF!"])
    n = state.randint(1, 10)
    return state.choice([".", "-", "_", "/", " ", "\n", "\n\r"])*n


def add_nan_like_artefacts(csv: pd.DataFrame, state: Random) -> pd.DataFrame:
    return csv.applymap(lambda x: random_nan(state) if pd.isna(x) else x)
