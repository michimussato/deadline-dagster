.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/My-Skeleton-Package.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/My-Skeleton-Package
    .. image:: https://readthedocs.org/projects/My-Skeleton-Package/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://My-Skeleton-Package.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/My-Skeleton-Package/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/My-Skeleton-Package
    .. image:: https://img.shields.io/pypi/v/My-Skeleton-Package.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/My-Skeleton-Package/
    .. image:: https://img.shields.io/conda/vn/conda-forge/My-Skeleton-Package.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/My-Skeleton-Package
    .. image:: https://pepy.tech/badge/My-Skeleton-Package/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/My-Skeleton-Package
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/My-Skeleton-Package

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

================
dagster-job-processor
================


    Add a short description here!


Installation
============

Clone and Install
-----------------

.. code-block:: shell

    git clone https://github.com/michimussato/dagster-job-processor.git
    cd dagster-job-processor
    python3.11 -m venv .venv
    source .venv/bin/activate
    pip install -e .[dev]


Run Dagster Dev
---------------

.. code-block:: shell

   cd dagster-job-processor
   export DAGSTER_HOME="$(pwd)/dagster/materializations"

   source .venv/bin/activate
   dagster dev --workspace "$(pwd)/dagster/workspace.yaml"



Install into venv
-----------------

.. code-block:: shell

    source .venv/bin/activate
    python -m pip install "dagster-job-processor[dev] @ git+https://github.com/michimussato/dagster-job-processor.git@main"

.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.6. For details and usage
information on PyScaffold see https://pyscaffold.org/.
