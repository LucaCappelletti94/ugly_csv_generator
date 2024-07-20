"""Test that the format of the version is correct."""

from validate_version_code import validate_version_code
from ugly_csv_generator.__version__ import __version__


def test_version():
    """Test that the format of the version is correct."""
    assert validate_version_code(__version__)
