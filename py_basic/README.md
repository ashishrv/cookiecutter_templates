# Python Project Cookie Cutter

## What is this?

Template for any python project

## Tools used in this project

* Poetry
* pdoc
* pytest


## Project Structure

```
.
├── .gitignore
├── CHANGELOG.md
├── README.md
├── makefile
├── poetry.toml
├── pyproject.toml
├── src
│   ├── scripts
│   │   ├── fix_dot_env_file.py
│   │   └── versioning.py
│   └── {{cookiecutter.package_name}}
│       └── __init__.py
└── tests
    └── __init__.py
```

## How to use this project

Install Cookiecutter:

```
python3 -m pip install --user cookiecutter
```

Create a project based on the template:

```
cookiecutter https://github.com/ashishrv/cookiecutter_templates.git/py_basic
```
