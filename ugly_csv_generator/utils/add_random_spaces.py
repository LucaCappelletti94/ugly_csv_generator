"""Randomly add spaces, newlines, and carriage returns to a CSV file.

This submodule provides a function to add random spaces,
newlines, and carriage returns to a CSV file.
"""

from random import Random
import pandas as pd


def random_space(state: Random):
    """Generate a random space-like artefact.

    Parameters
    --------------------------
    state: Random,
        The random state to use for the generation.
    """
    k = state.randint(1, 10)
    return "".join(state.choices([" ", "\n", "\n\r"], [0.8, 0.15, 0.05], k=k))


def add_random_spaces(csv: pd.DataFrame, state: Random) -> pd.DataFrame:
    """Add random spaces, newlines, and carriage returns to the provided DataFrame.

    Parameters
    --------------------------
    csv: pd.DataFrame,
        The DataFrame to add the random spaces, newlines, and carriage returns to.
    state: Random,
        The random state to use for the generation.
    """
    return csv.map(
        lambda x: (
            f"{random_space(state)}{str(x).replace(' ', random_space(state))}{random_space(state)}"
            if not pd.isna(x)
            else x
        )
    )
