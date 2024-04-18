"""Configuration for pytest."""

from __future__ import annotations

import pytest


@pytest.fixture(autouse=True)
def _add_standard_imports(doctest_namespace):
    """Add {{cookiecutter.pkg_name}} namespace for doctest."""
    import {{cookiecutter.pkg_name}} as {{cookiecutter.pkg_short_name}}

    doctest_namespace["{{cookiecutter.pkg_short_name}}"] = {{cookiecutter.pkg_short_name}}
