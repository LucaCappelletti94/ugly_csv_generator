"""Test to verify that all characters lists used throughout the package are unique."""

from ugly_csv_generator.utils.replace_zeros import (
    ZERO_LOOKING_CHARACTERS,
    UNICODE_ZERO_LOOKING_CHARACTERS,
)
from ugly_csv_generator.utils.add_nan_like_artefacts import (
    NAN_LIKE_ARTIFACTS,
    UNICODE_NAN_LIKE_ARTIFACTS,
)
from ugly_csv_generator.utils.add_random_spaces import (
    UNICODE_SPACES,
    SPACES,
)
from ugly_csv_generator.utils.replace_ones import (
    ONE_LOOKING_CHARACTERS,
    UNICODE_ONE_LOOKING_CHARACTERS,
)


def test_uniqueness():
    """Test to verify that all characters lists used throughout the package are unique."""
    assert len(ZERO_LOOKING_CHARACTERS) == len(
        set(ZERO_LOOKING_CHARACTERS)
    ), "The ZERO_LOOKING_CHARACTERS list is not unique."
    assert len(UNICODE_ZERO_LOOKING_CHARACTERS) == len(
        set(UNICODE_ZERO_LOOKING_CHARACTERS)
    ), "The UNICODE_ZERO_LOOKING_CHARACTERS list is not unique."
    assert len(NAN_LIKE_ARTIFACTS) == len(
        set(NAN_LIKE_ARTIFACTS)
    ), "The NAN_LIKE_ARTIFACTS list is not unique."
    assert len(UNICODE_NAN_LIKE_ARTIFACTS) == len(
        set(UNICODE_NAN_LIKE_ARTIFACTS)
    ), "The UNICODE_NAN_LIKE_ARTIFACTS list is not unique."
    assert len(UNICODE_SPACES) == len(
        set(UNICODE_SPACES)
    ), "The UNICODE_SPACES list is not unique."
    assert len(SPACES) == len(set(SPACES)), "The SPACES list is not unique."
    assert len(ONE_LOOKING_CHARACTERS) == len(
        set(ONE_LOOKING_CHARACTERS)
    ), "The ONE_LOOKING_CHARACTERS list is not unique."
    assert len(UNICODE_ONE_LOOKING_CHARACTERS) == len(
        set(UNICODE_ONE_LOOKING_CHARACTERS)
    ), "The UNICODE_ONE_LOOKING_CHARACTERS list is not unique."
