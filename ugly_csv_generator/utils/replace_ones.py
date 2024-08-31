"""Submodule providing a method to replace ones in a dataframe with one-looking characters."""

from random import Random
from typing import List
import pandas as pd
from ugly_csv_generator.utils.replace_character import replace_character

ONE_LOOKING_CHARACTERS: List[str] = ["I", "l", "1"]

UNICODE_ONE_LOOKING_CHARACTERS: List[str] = [
    "\uFF11",  # FULLWIDTH DIGIT ONE
    "\u2460",  # CIRCLED DIGIT ONE
    "\u24F5",  # DOUBLE CIRCLED DIGIT ONE
    "\u2776",  # DINGBAT NEGATIVE CIRCLED DIGIT ONE
    "\U0001D7D9",  # MATHEMATICAL DOUBLE-STRUCK DIGIT ONE
    "\U0001D7CF",  # MATHEMATICAL BOLD DIGIT ONE
    "\u00B9",  # SUPERSCRIPT ONE
    "\u2081",  # SUBSCRIPT ONE
    "\u00B9",  # SUPERSCRIPT ONE
]


def replace_ones(
    csv: pd.DataFrame, state: Random, include_unicode: bool
) -> pd.DataFrame:
    """Replace ones in a dataframe with one-looking characters.

    Parameters
    --------------------------
    csv: pd.DataFrame,
        The DataFrame to add the NaN-like artefacts to.
    state: Random,
        The random state to use for the generation.
    include_unicode: bool,
        Whether to include Unicode one-looking characters.
    """
    return replace_character(
        csv,
        state,
        "1",
        (
            (UNICODE_ONE_LOOKING_CHARACTERS + ONE_LOOKING_CHARACTERS)
            if include_unicode
            else ONE_LOOKING_CHARACTERS
        ),
    )
