# Python Project Cookie Cutter

## What is this?

Template for cli python project

## Tools used in this project

* Poetry
* pdoc
* pytest
* typer

## Project Structure

```
.
.
├── LICENSE
├── README.md
├── cookiecutter.json
└── {{cookiecutter.package_name}}
    ├── CHANGELOG.md
    ├── README.md
    ├── docs
    ├── makefile
    ├── poetry.toml
    ├── pyproject.toml
    ├── src
    │  ├── scripts
    │  │  ├── fix_dot_env_file.py
    │  │  └── versioning.py
    │  └── {{cookiecutter.package_name}}
    │      ├── __init__.py
    │      └── cli
    │          ├── __init__.py
    │          ├── items.py
    │          └── users.py
    └── tests
        ├── __init__.py
        └── test_dummy.py
```

## How to use this project

Install Cookiecutter:

```
python3 -m pip install --user cookiecutter
```

Create a project based on the template:

```
cookiecutter https://github.com/ashishrv/cookiecutter_templates.git/py_cli
```
