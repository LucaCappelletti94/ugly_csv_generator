"""Randomly add spaces, newlines, and carriage returns to a CSV file.

This submodule provides a function to add random spaces,
newlines, and carriage returns to a CSV file.
"""

from random import Random
import pandas as pd

SPACES = [" ", "\t", "\n", "\n\r"]

UNICODE_SPACES = [
    "\u0020",  # ASCII space, should be the same as ' '
    "\u00A0",  # Non-breaking space
    "\u1680",  # Ogham space mark
    "\u2000",  # En quad
    "\u2001",  # Em quad
    "\u2002",  # En space
    "\u2003",  # Em space
    "\u2004",  # Three-per-em space
    "\u2005",  # Four-per-em space
    "\u2006",  # Six-per-em space
    "\u2007",  # Figure space
    "\u2008",  # Punctuation space
    "\u2009",  # Thin space
    "\u200A",  # Hair space
    "\u200B",  # Zero-width space
    "\u200C",  # Zero-width non-joiner
    "\u200D",  # Zero-width joiner
    "\u202F",  # Narrow no-break space
    "\u205F",  # Medium mathematical space
    "\u3000",  # Ideographic space
    "\uFEFF",  # Zero-width non-breaking space
    "\u180E",  # Mongolian vowel separator
    "\u2060",  # Word joiner
    "\u2063",  # Invisible separator
    "\U000E0020",  # Tag space
    "\u001C",  # File separator
    "\u001D",  # Group separator
    "\u001E",  # Record separator
    "\u001F",  # Unit separator
] + SPACES


def random_space(state: Random, include_unicode: bool):
    """Generate a random space-like artefact.

    Parameters
    --------------------------
    state: Random,
        The random state to use for the generation.
    include_unicode: bool,
        Whether to include Unicode space-like artefacts.

    Returns
    --------------------------
    A random space-like artefact.
    """
    k = state.randint(1, 10)
    return "".join(state.choices(UNICODE_SPACES if include_unicode else SPACES, k=k))


def add_random_spaces(
    csv: pd.DataFrame, state: Random, include_unicode: bool
) -> pd.DataFrame:
    """Add random spaces, newlines, and carriage returns to the provided DataFrame.

    Parameters
    --------------------------
    csv: pd.DataFrame,
        The DataFrame to add the random spaces, newlines, and carriage returns to.
    state: Random,
        The random state to use for the generation.
    include_unicode: bool,
        Whether to include Unicode space-like artefacts.
    """
    return csv.map(
        lambda x: (
            f"{random_space(state, include_unicode)}{str(x).replace(' ', random_space(state, include_unicode))}{random_space(state, include_unicode)}"
            if not pd.isna(x)
            else x
        )
    )
