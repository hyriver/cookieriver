"""Top-level package for {{cookiecutter.pkg_name}}."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from {{cookiecutter.pkg_name}}.{{cookiecutter.pkg_name}} import function
from {{cookiecutter.pkg_name}}.print_versions import show_versions

try:
    __version__ = version("{{cookiecutter.pkg_name}}")
except PackageNotFoundError:
    __version__ = "999"

__all__ = ["function", "show_versions", "__version__"]
