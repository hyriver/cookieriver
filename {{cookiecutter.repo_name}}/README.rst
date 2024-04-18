{{cookiecutter.repo_name}}: {{cookiecutter.repo_title}}
=============================================================

.. image:: https://img.shields.io/pypi/v/{{cookiecutter.repo_name}}.svg
    :target: https://pypi.python.org/pypi/{{cookiecutter.repo_name}}
    :alt: PyPi

.. image:: https://img.shields.io/conda/vn/conda-forge/{{cookiecutter.repo_name}}.svg
    :target: https://anaconda.org/conda-forge/{{cookiecutter.repo_name}}
    :alt: Conda Version

.. image:: https://codecov.io/gh/hyriver/{{cookiecutter.repo_name}}/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/hyriver/{{cookiecutter.repo_name}}
    :alt: CodeCov

.. image:: https://img.shields.io/pypi/pyversions/{{cookiecutter.repo_name}}.svg
    :target: https://pypi.python.org/pypi/{{cookiecutter.repo_name}}
    :alt: Python Versions

.. image:: https://static.pepy.tech/badge/{{cookiecutter.repo_name}}
    :target: https://pepy.tech/project/{{cookiecutter.repo_name}}
    :alt: Downloads

|

.. image:: https://img.shields.io/badge/security-bandit-green.svg
    :target: https://github.com/PyCQA/bandit
    :alt: Security Status

.. image:: https://www.codefactor.io/repository/github/hyriver/{{cookiecutter.repo_name}}r/badge
   :target: https://www.codefactor.io/repository/github/hyriver/{{cookiecutter.repo_name}}
   :alt: CodeFactor

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
    :target: https://github.com/pre-commit/pre-commit
    :alt: pre-commit

|

Features
--------

Citation
--------
If you use any of HyRiver packages in your research, we appreciate citations:

.. code-block:: bibtex

    @article{Chegini_2021,
        author = {Chegini, Taher and Li, Hong-Yi and Leung, L. Ruby},
        doi = {10.21105/joss.03175},
        journal = {Journal of Open Source Software},
        month = {10},
        number = {66},
        pages = {1--3},
        title = {% raw %}{{HyRiver: Hydroclimate Data Retriever}}{% endraw %},
        volume = {6},
        year = {2021}
    }

Installation
------------
You can install ``{{cookiecutter.pkg_name}}`` using ``pip``:

.. code-block:: console

    $ pip install {{cookiecutter.pkg_name}}

Alternatively, ``{{cookiecutter.pkg_name}}`` can be installed from the ``conda-forge`` repository
using `micromamba <https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html/>`__:

.. code-block:: console

    $ micromamba install -c conda-forge {{cookiecutter.pkg_name}}


Quick start
-----------

Contributing
------------
Contributions are appreciated and very welcomed. Please read
`CONTRIBUTING.rst <https://github.com/hyriver/{{cookiecutter.repo_name}}/blob/main/CONTRIBUTING.rst>`__
for instructions.
