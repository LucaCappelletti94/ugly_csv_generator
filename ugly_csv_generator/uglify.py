import pandas as pd
import numpy as np
from random import Random
from .utils import add_empty_columns, add_empty_rows, add_duplicate_schema, add_empty_padding


def uglify(
    csv: pd.DataFrame,
    path: str = None,
    empty_columns: bool = True,
    empty_rows: bool = True,
    duplicate_schema: bool = True,
    empty_padding: bool = True,
    excel_like_artefacts: bool = True,
    nan_like_artefacts: bool = True,
    # random_separator: bool = True,
    # random_spaces: bool = True,
    seed: int = 42
):
    """Return or saves to given path an uglified version of the given DataFrame.

    The procedure is non-destructive,
    meaning all infomation should remain retrievable
    using a valid reconstruction method.

    Parameters
    ---------------------------------
    csv:pd.DataFrame,
        The dataframe containing the CSV to uglify.
    path:str=None,
        Path where to save the CSV.
    empty_columns:bool=True,
        Whetever to introduce empty columns (with header).
    empty_padding:bool=True,
        Whetever to introduce padding around the data.
    random_separator:bool=True,
        Whetever to use a random separator when saving the file.
    random_spaces:bool=True,
        Whetever to add random spaces to the file values.
    empty_rows:bool=True,
        Whetever to introduce random blank rows.
    duplicate_schema:bool=True,
        Whetever to duplicate the schema rows within the data.
    excel_like_artefacts:bool=True,
        Whetever to add excel-like artefacts.
    nan_like_artefacts:bool=True,
        Whetever to add nan-like artefacts.
    seed:int=42
        The random seed to use to make reproducible the random aspects.

    Returns
    --------------------------------
    The uglified dataframe.
    """
    state = Random(seed)
    if empty_columns:
        csv = add_empty_columns(csv.copy(), state)

    if empty_rows:
        csv = add_empty_rows(csv, state)

    if duplicate_schema:
        csv = add_duplicate_schema(csv, state)

    if empty_padding:
        csv = add_empty_padding(csv, state)
    
    return csv