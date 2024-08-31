"""Submodule providing a method to replace zeros in a dataframe with zero-looking characters."""

from random import Random
from typing import List
import pandas as pd
from ugly_csv_generator.utils.replace_character import replace_character

ZERO_LOOKING_CHARACTERS: List[str] = ['O', 'o', '0']

UNICODE_ZERO_LOOKING_CHARACTERS: List[str] = [
    '\uFF10',  # FULLWIDTH DIGIT ZERO
    '\u24EA',  # CIRCLED DIGIT ZERO
    '\u24FF',  # NEGATIVE CIRCLED DIGIT ZERO
    '\U0001D7D8',  # MATHEMATICAL DOUBLE-STRUCK DIGIT ZERO
    '\U0001D7CE',  # MATHEMATICAL BOLD DIGIT ZERO
    '\u2070',  # SUPERSCRIPT ZERO
    '\u2080',  # SUBSCRIPT ZERO
    '\u03BF',  # GREEK SMALL LETTER OMICRON
    '\u1D0F',  # LATIN LETTER SMALL CAPITAL O
    '\u1D11',  # LATIN SMALL LETTER SIDEWAYS O
    '\u1D13',  # LATIN SMALL LETTER TURNED O
    '\u1D52',  # MODIFIER LETTER SMALL O
    '\u041E',  # CYRILLIC CAPITAL LETTER O
    '\u043E',  # CYRILLIC SMALL LETTER O
    '\u0555',  # ARMENIAN CAPITAL LETTER VO
    '\u0585',  # ARMENIAN SMALL LETTER VO
    '\u0660',  # ARABIC-INDIC DIGIT ZERO
    '\u06F0',  # EXTENDED ARABIC-INDIC DIGIT ZERO (Persian)
    '\u07C0',  # NKO DIGIT ZERO
    '\u0E50',  # THAI DIGIT ZERO
    '\u0ED0',  # LAO DIGIT ZERO
    '\u0F20',  # TIBETAN DIGIT ZERO
    '\u1040',  # MYANMAR DIGIT ZERO
    '\u17E0',  # KHMER DIGIT ZERO
    '\u1810',  # MONGOLIAN DIGIT ZERO
    '\u1946',  # LIMBU DIGIT ZERO
    '\u19D0',  # NEW TAI LUE DIGIT ZERO
    '\u1A80',  # TAI THAM HORA DIGIT ZERO
    '\u1A90',  # TAI THAM THAM DIGIT ZERO
    '\u1B50',  # BALINESE DIGIT ZERO
    '\u1BB0',  # SUNDANESE DIGIT ZERO
    '\u1C40',  # LEPCHA DIGIT ZERO
    '\u1C50',  # OL CHIKI DIGIT ZERO
]


def replace_zeros(
    csv: pd.DataFrame, state: Random, include_unicode: bool
) -> pd.DataFrame:
    """Replace zeros in a dataframe with zero-looking characters.

    Parameters
    --------------------------
    csv: pd.DataFrame,
        The DataFrame to add the NaN-like artefacts to.
    state: Random,
        The random state to use for the generation.
    include_unicode: bool,
        Whether to include Unicode zero-looking characters.
    """
    return replace_character(
        csv,
        state,
        [0, 0.0, '0'],
        (UNICODE_ZERO_LOOKING_CHARACTERS + ZERO_LOOKING_CHARACTERS) if include_unicode else ZERO_LOOKING_CHARACTERS,
    )
