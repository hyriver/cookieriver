"""Command-line interface for {{cookiecutter.pkg_name}}."""

from __future__ import annotations

from pathlib import Path

import click


CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}

@click.group(context_settings=CONTEXT_SETTINGS)
def cli() -> None:
    """Command-line interface for {{cookiecutter.pkg_name}}."""

@cli.command("command1", context_settings=CONTEXT_SETTINGS)
@click.argument("fpath", type=click.Path(exists=True))
@click.option(
    "-s",
    "--save_dir",
    default="data",
    type=click.Path(exists=False),
    help="Path to a directory to save the requested files.",
)
def command1(
    fpath: Path,
    save_dir: str | Path = "data",
) -> None:
    """Retrieve data.

    \b
    FPATH: Path to input file.

    \b
    Examples:
        $ {{cookiecutter.pkg_name}} command1 input_file -s data
    """  # noqa: D301
    fpath = Path(fpath)
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    click.echo("Done.")


@cli.command("command2", context_settings=CONTEXT_SETTINGS)
@click.argument("fpath", type=click.Path(exists=True))
@click.option(
    "-s",
    "--save_dir",
    default="data",
    type=click.Path(exists=False),
    help="Path to a directory to save the requested files.",
)
def command2(
    fpath: Path,
    save_dir: str | Path = "data",
) -> None:
    """Retrieve data.

    \b
    FPATH: Path to input file.

    \b
    Examples:
        $ {{cookiecutter.pkg_name}} command2 input_file -s data
    """  # noqa: D301
    fpath = Path(fpath)
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    click.echo("Done.")
