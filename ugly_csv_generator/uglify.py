import pandas as pd
from random import Random
from .utils import (
    add_empty_columns, add_empty_rows, add_duplicate_schema,
    add_empty_padding, add_nan_like_artefacts, add_random_spaces,
    add_satellites
)


def uglify(
    csv: pd.DataFrame,
    # path: str = None,
    empty_columns: bool = True,
    empty_rows: bool = True,
    duplicate_schema: bool = True,
    empty_padding: bool = True,
    nan_like_artefacts: bool = True,
    # random_separator: bool = True,
    satellite_artefacts: bool = True,
    random_spaces: bool = True,
    verbose: bool = True,
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
    satellite_artefacts:bool=True,
        Whetever to add satellite text around the central table.
        This is useful to simulate when you can expect for
        random scribbling around your CSV data.
        The satellites may be added on the top or bottom.
    random_spaces:bool=True,
        Whetever to add random spaces to the file values.
    empty_rows:bool=True,
        Whetever to introduce random blank rows.
    duplicate_schema:bool=True,
        Whetever to duplicate the schema rows within the data.
    verbose: bool = True,
        Whetever to show the loading bars.
    seed:int=42
        The random seed to use to make reproducible the random aspects.

    Returns
    --------------------------------
    The uglified dataframe.
    """
    state = Random(seed)

    if duplicate_schema:
        csv = add_duplicate_schema(csv, state, verbose=verbose)

    if random_spaces:
        csv = add_random_spaces(csv, state)

    if empty_columns:
        csv = add_empty_columns(csv.copy(), state, verbose=verbose)

    if empty_rows:
        csv = add_empty_rows(csv, state, verbose=verbose)

    if empty_padding:
        csv = add_empty_padding(csv, state)

    if satellite_artefacts:
        csv = add_satellites(csv, state)

    if nan_like_artefacts:
        csv = add_nan_like_artefacts(csv, state)

    return csv
