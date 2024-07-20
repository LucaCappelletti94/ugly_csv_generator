"""Submodule providing utilities to add artefacts to a CSV."""

from ugly_csv_generator.utils.add_empty_columns import add_empty_columns
from ugly_csv_generator.utils.add_empty_rows import add_empty_rows
from ugly_csv_generator.utils.add_duplicate_schema import add_duplicate_schema
from ugly_csv_generator.utils.add_empty_padding import add_empty_padding
from ugly_csv_generator.utils.add_nan_like_artefacts import add_nan_like_artefacts
from ugly_csv_generator.utils.add_random_spaces import add_random_spaces
from ugly_csv_generator.utils.add_satellites import add_satellites

__all__ = [
    "add_empty_columns",
    "add_empty_rows",
    "add_duplicate_schema",
    "add_empty_padding",
    "add_nan_like_artefacts",
    "add_random_spaces",
    "add_satellites",
]
