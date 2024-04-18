# CookieRiver: Cookiecutter Template for HyRiver Software Development

This is a [Cookiecutter](https://cookiecutter.readthedocs.io) template for HyRiver software development. It generates a project structure with the following features:

- A Python package with a command-line interface (CLI) using [Click](https://click.palletsprojects.com)
- A test suite using [pytest](https://docs.pytest.org)
- Continuous integration (CI) using [GitHub Actions](https://docs.github.com/en/actions)
- Code coverage using [Codecov](https://about.codecov.io)
- A README template with badges for CI, code coverage, and PyPI
- An MIT [LICENSE](https://choosealicense.com) file
- Contribution and Code of Conduct guidelines
- A `pyproject.toml` file
- Linting, formatting, and type checking using [pre-commit](https://pre-commit.com),
  [pyright](https://microsoft.github.io/pyright/), and [nox](https://nox.thea.codes)

## Usage

First, install `cookiecutter`:

```bash
pipx install cookiecutter
```

Then, generate a new project:

```bash
cookiecutter gh:hyriver/cookieriver
```
