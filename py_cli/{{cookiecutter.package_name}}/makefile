

.PHONY: docs help

# Exports all variables defined in the makefile available to scripts
.EXPORT_ALL_VARIABLES:

# Create .env file if it does not already exist
ifeq (,$(wildcard .env))
  $(shell touch .env)
endif

# Includes environment variables from the .env file
include .env


help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install-poetry:
	@echo "Installing poetry..."
	@curl -sSL https://install.python-poetry.org | python3  -
	@$(eval include ${HOME}/.poetry/env)
	@poetry self update

uninstall-poetry:
	@echo "Uninstalling poetry..."
	@curl -sSL https://install.python-poetry.org | POETRY_UNINSTALL=1 python3 -


install: ## Install dependencies
	@echo "Installing..."
	@if [ "$(shell which poetry)" = "" ]; then \
		$(MAKE) install-poetry; \
	fi
	@if [ "$(shell which gpg)" = "" ]; then \
		echo "GPG not installed, so an error will occur. Install GPG on MacOS with "\
			 "`brew install gnupg` or on Ubuntu with `apt install gnupg` and run "\
			 "`make install` again."; \
	fi
	@$(MAKE) setup-poetry
	#@$(MAKE) setup-environment-variables
	@$(MAKE) setup-git

setup-poetry:
	@echo "Setting up library dependencies ..."
	@poetry env use python3 && poetry install

setup-environment-variables:
	@echo "Fixing .env file ..."
	@poetry run python3 -m src.scripts.fix_dot_env_file


setup-git-gpg:
	@if [ ${GPG_KEY_ID} = "" ]; then \
		echo "No GPG key ID specified. Skipping GPG signing."; \
		git config --local commit.gpgsign false; \
	else \
		echo "Signing with GPG key ID ${GPG_KEY_ID}..."; \
		echo 'Just for info: If you get the "failed to sign the data" error when '\
			 'committing, try running `export GPG_TTY=$$(tty)` and `gpgconf --kill '\
			 'gpg-agent`, and try again.'; \
		git config --local commit.gpgsign true; \
		git config --local user.signingkey ${GPG_KEY_ID}; \
	fi

setup-git-config:
	#@git config --local user.name ${GIT_NAME}
	#@git config --local user.email ${GIT_EMAIL}
	@git ${GIT_TYPE}

setup-git:
	@git init
	#@$(MAKE) setup-git-config
	#@$(MAKE) setup-git-gpg
	@poetry run pre-commit install

docs:  ## Generate documentation
	@poetry run pdoc --docformat google src/{{cookiecutter.package_name}} -o docs
	@echo "Saved documentation."

view-docs:  ## View documentation
	@echo "Viewing API documentation..."
	@uname=$$(uname); \
		case $${uname} in \
			(*Linux*) openCmd='xdg-open'; ;; \
			(*Darwin*) openCmd='open'; ;; \
			(*CYGWIN*) openCmd='cygstart'; ;; \
			(*) echo 'Error: Unsupported platform: $${uname}'; exit 2; ;; \
		esac; \
		"$${openCmd}" docs/{{ cookiecutter.package_name }}.html

bump-major:
	@poetry run python3 -m src.scripts.versioning --major
	@echo "Bumped major version!"

bump-minor:
	@poetry run python3 -m src.scripts.versioning --minor
	@echo "Bumped minor version!"

bump-patch:
	@poetry run python3 -m src.scripts.versioning --patch
	@echo "Bumped patch version!"

publish:
	@if [ ${PYPI_API_TOKEN} = "" ]; then \
		echo "No PyPI API token specified in the '.env' file, so cannot publish."; \
	else \
		echo "Publishing to PyPI..."; \
		poetry publish --build --username "__token__" --password ${PYPI_API_TOKEN}; \
	fi
	@echo "Published!"

publish-major: bump-major publish  ## Publish a major version

publish-minor: bump-minor publish  ## Publish a minor version

publish-patch: bump-patch publish  ## Publish a patch version

build:
	@echo "Building package .....";
	poetry build
	@echo "Package built"

build-major: bump-major build  ## Publish a major version

build-minor: bump-minor build  ## Publish a minor version

build-patch: bump-patch build  ## Publish a patch version

test:  ## Run tests
	@poetry run pytest && readme-cov

lint: ## Run linters
	@echo
	@poetry run ruff src/{{cookiecutter.package_name}}
	@echo
	@poetry run blue --check --diff --color src/{{cookiecutter.package_name}}
	@echo
	@poetry run mypy src/{{cookiecutter.package_name}}
	@echo
	@poetry run pip-audit src/{{cookiecutter.package_name}}

format: ## Run code formatters
	@poetry run ruff --silent --exit-zero --fix src/{{cookiecutter.package_name}}
	@poetry run blue src/{{cookiecutter.package_name}}

tree:  ## Print directory tree
	@tree -a \
		-I .git \
		-I .mypy_cache \
		-I .env \
		-I .venv \
		-I poetry.lock \
		-I dist \
		-I .gitkeep \
		-I docs \
		-I .pytest_cache \
		-I outputs \
		-I .DS_Store \
		-I .cache \
		-I raw \
		-I processed \
		-I final \
		-I checkpoint-* \
		-I .coverage* \
		-I .DS_Store \
		-I __pycache__ \
		.
