"""Submodule to add NaN-like artefacts to a csv file."""

from random import Random
import pandas as pd
import numpy as np
from ugly_csv_generator.utils.add_random_spaces import random_space
from ugly_csv_generator.utils.replace_zeros import (
    ZERO_LOOKING_CHARACTERS,
    UNICODE_ZERO_LOOKING_CHARACTERS,
)

NAN_LIKE_ARTIFACTS = [np.nan, "#RIF!", "N/A"] + ZERO_LOOKING_CHARACTERS

UNICODE_NAN_LIKE_ARTIFACTS = [
    "\uFFFD",  # REPLACEMENT CHARACTER
    "\u221E",  # INFINITY
    "\u29DC",  # INCOMPLETE INFINITY
    "\u003F",  # QUESTION MARK
    "\u00BF",  # INVERTED QUESTION MARK
    "\u2216",  # SET MINUS
    "\u65E0",  # CJK UNIFIED IDEOGRAPH representing "none"
] + UNICODE_ZERO_LOOKING_CHARACTERS


def random_nan(state: Random, include_unicode: bool) -> str:
    """Generate a random NaN-like artefact.

    Parameters
    --------------------------
    state: Random,
        The random state to use for the generation.
    """
    if state.randint(0, 1) == 1:
        return state.choice((UNICODE_NAN_LIKE_ARTIFACTS + NAN_LIKE_ARTIFACTS) if include_unicode else NAN_LIKE_ARTIFACTS)
    n = state.randint(1, 10)
    return (
        state.choice([".", "-", "_", "/", random_space(state, include_unicode=False)])
        * n
    )


def add_nan_like_artefacts(
    csv: pd.DataFrame, state: Random, include_unicode: bool
) -> pd.DataFrame:
    """Add NaN-like artefacts to the provided DataFrame.

    Parameters
    --------------------------
    csv: pd.DataFrame,
        The DataFrame to add the NaN-like artefacts to.
    state: Random,
        The random state to use for the generation.
    include_unicode: bool,
        Whether to include Unicode NaN-like artefacts.
    """
    return csv.map(
        lambda x: (
            random_nan(state, include_unicode=include_unicode) if pd.isna(x) else x
        )
    )
