"""Module providing the uglify function to uglify a CSV."""

from typing import Union
from random import Random
import pandas as pd
from ugly_csv_generator.utils import (
    add_empty_columns,
    add_empty_rows,
    add_duplicate_schema,
    add_empty_padding,
    add_nan_like_artefacts,
    add_random_spaces,
    add_satellites,
)


def uglify(
    csv: Union[pd.DataFrame, str],
    empty_columns: bool = True,
    empty_rows: bool = True,
    duplicate_schema: bool = True,
    empty_padding: bool = True,
    nan_like_artefacts: bool = True,
    satellite_artefacts: bool = False,
    random_spaces: bool = True,
    verbose: bool = True,
    seed: int = 42,
):
    """Return or saves to given path an uglified version of the given DataFrame.

    The procedure is non-destructive,
    meaning all infomation should remain retrievable
    using a valid reconstruction method.

    Parameters
    ---------------------------------
    csv: pd.DataFrame,
        The dataframe containing or path to the CSV to uglify.
    empty_columns: bool = True,
        Whether to introduce empty columns (with header).
    empty_rows: bool = True,
        Whether to introduce random blank rows.
    duplicate_schema: bool = True,
        Whether to duplicate the schema rows within the data.
    empty_padding: bool = True,
        Whether to introduce padding around the data.
    nan_like_artefacts: bool = True,
        Whether to introduce NaN-like artefacts.
        A NaN-like artefact is a value that looks like NaN
        but is not actually NaN, like "N/A" or "-".
    satellite_artefacts: bool = True,
        Whether to add satellite text around the central table.
        This is useful to simulate when you can expect for
        random scribbling around your CSV data.
        The satellites may be added on the top or bottom.
        It selects a random satellite from the available satellites
        collection in the package, encountered in the real world.
    random_spaces: bool = True,
        Whether to add random spaces to the file values.
    verbose: bool = True,
        Whether to show the loading bars.
    seed: int = 42
        The random seed to use to make reproducible the random aspects.

    Returns
    --------------------------------
    The uglified dataframe.
    """
    state = Random(seed)

    # If the CSV is a path, load it
    if isinstance(csv, str):
        csv = pd.read_csv(csv)

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
