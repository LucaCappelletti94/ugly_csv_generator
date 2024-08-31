"""Submodule providing a method to replace ones in a dataframe with one-looking characters."""

from random import Random
from typing import List
import pandas as pd
from ugly_csv_generator.utils.replace_character import replace_character

ONE_LOOKING_CHARACTERS: List[str] = ['I', 'l', '1']

UNICODE_ONE_LOOKING_CHARACTERS: List[str] = [
    '\uFF11',  # FULLWIDTH DIGIT ONE
    '\u2460',  # CIRCLED DIGIT ONE
    '\u24F5',  # DOUBLE CIRCLED DIGIT ONE
    '\u2776',  # DINGBAT NEGATIVE CIRCLED DIGIT ONE
    '\U0001D7D9',  # MATHEMATICAL DOUBLE-STRUCK DIGIT ONE
    '\U0001D7CF',  # MATHEMATICAL BOLD DIGIT ONE
    '\u2081',  # SUBSCRIPT ONE
    '\u00B9',  # SUPERSCRIPT ONE
    '\u0661',  # ARABIC-INDIC DIGIT ONE
    '\u06F1',  # EXTENDED ARABIC-INDIC DIGIT ONE (Persian)
    '\u07C1',  # NKO DIGIT ONE
    '\u0967',  # DEVANAGARI DIGIT ONE
    '\u09E7',  # BENGALI DIGIT ONE
    '\u0A67',  # GURMUKHI DIGIT ONE
    '\u0AE7',  # GUJARATI DIGIT ONE
    '\u0B67',  # ORIYA DIGIT ONE
    '\u0BE7',  # TAMIL DIGIT ONE
    '\u0C67',  # TELUGU DIGIT ONE
    '\u0CE7',  # KANNADA DIGIT ONE
    '\u0D67',  # MALAYALAM DIGIT ONE
    '\u0E51',  # THAI DIGIT ONE
    '\u0ED1',  # LAO DIGIT ONE
    '\u0F21',  # TIBETAN DIGIT ONE
    '\u1041',  # MYANMAR DIGIT ONE
    '\u17E1',  # KHMER DIGIT ONE
    '\u1811',  # MONGOLIAN DIGIT ONE
    '\u1947',  # LIMBU DIGIT ONE
    '\u19D1',  # NEW TAI LUE DIGIT ONE
    '\u1A81',  # TAI THAM HORA DIGIT ONE
    '\u1A91',  # TAI THAM THAM DIGIT ONE
    '\u1B51',  # BALINESE DIGIT ONE
    '\u1BB1',  # SUNDANESE DIGIT ONE
    '\u1C41',  # LEPCHA DIGIT ONE
    '\u1C51',  # OL CHIKI DIGIT ONE
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
        ["1", 1, 1.0],
        (
            (UNICODE_ONE_LOOKING_CHARACTERS + ONE_LOOKING_CHARACTERS)
            if include_unicode
            else ONE_LOOKING_CHARACTERS
        ),
    )
