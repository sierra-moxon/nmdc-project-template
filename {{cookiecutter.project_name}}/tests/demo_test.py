"""Demo version test."""

import pytest

from {{cookiecutter.__project_slug}} import __version__


def test_version_type():
    """Demo test."""
    assert type(__version__) == str
