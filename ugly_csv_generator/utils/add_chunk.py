import pandas as pd

def add_chunk(csv: pd.DataFrame, chunk: pd.DataFrame, iloc: int):
    return pd.concat([
        csv.iloc[:iloc],
        chunk,
        csv.iloc[iloc:]
    ]).reset_index(drop=True)