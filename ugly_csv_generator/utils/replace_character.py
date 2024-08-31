"""Submodule providing a method to replace randomly in a dataframe given a random state a character with ones from a provided list."""

from random import Random
from typing import List
import pandas as pd


def replace_character(
    csv: pd.DataFrame, state: Random, character: List[str], characters_to_replace: List[str]
) -> pd.DataFrame:
    """Replace randomly in a dataframe given a random state a character with ones from a provided list.

    Parameters
    --------------------------
    csv: pd.DataFrame,
        The DataFrame to add the NaN-like artefacts to.
    state: Random,
        The random state to use for the generation.
    character: List[str],
        The character to replace.
        E.g. in the case of zero it will be ['0', 0, 0.0].
    characters_to_replace: List[str],
        The list of characters to replace the character with.
    """
    assert (
        characters_to_replace
    ), "The list of characters to replace the character with cannot be empty."
    return csv.map(
        lambda x: (state.choice(characters_to_replace) if x in character else x)
    )
