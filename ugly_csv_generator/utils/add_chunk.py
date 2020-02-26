import pandas as pd
import numpy as np

def add_chunk(csv: pd.DataFrame, chunk: pd.DataFrame, iloc: int):
    if chunk.shape[1] < csv.shape[1]:
        old_chunk = chunk
        chunk = pd.DataFrame(np.nan, columns=csv.columns, index=old_chunk.index, dtype="object")
        chunk.values[:old_chunk.shape[0], :old_chunk.shape[1]] = old_chunk.values
    return pd.concat([
        csv.iloc[:iloc],
        chunk,
        csv.iloc[iloc:]
    ]).reset_index(drop=True)