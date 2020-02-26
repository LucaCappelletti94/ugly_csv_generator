from .add_row import add_row
import pandas as pd
import numpy as np
from random import Random
from tqdm.auto import tqdm


def add_duplicate_schema(csv: pd.DataFrame, state: Random, verbose:bool) -> pd.DataFrame:
    """Duplicate the schema into random new rows."""
    schema_number = state.randint(0, max(1, len(csv)//2))
    for _ in tqdm(range(schema_number), desc="Adding duplicated schemas", disable=not verbose):
        csv = add_row(csv, csv.columns, state=state)
    return csv
