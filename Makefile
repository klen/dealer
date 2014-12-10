VIRTUALENV=$(shell echo "$${VDIR:-'.env'}")

all: $(VIRTUALENV)

.PHONY: help
# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile

.PHONY: clean
# target: clean - Clean repo
clean:
	rm -rf build dist
	find . -name "*.pyc" -delete
	find . -name "*.orig" -delete
	find $(CURDIR)/$(MODULE) -name "__pycache__" | xargs rm -rf
	find $(CURDIR)/$(MODULE) -name "*.egg" | xargs rm -rf


# ==============
#  Bump version
# ==============

.PHONY: release
VERSION?=minor
# target: release - Bump version
release:
	@$(VIRTUALENV)/bin/pip install bumpversion
	@$(VIRTUALENV)/bin/bumpversion $(VERSION)
	@git checkout master
	@git merge develop
	@git checkout develop
	@git push --all
	@git push --tags

.PHONY: minor
minor: release

.PHONY: patch
patch:
	make release VERSION=patch

.PHONY: major
major:
	make release VERSION=major


# ===============
#  Build package
# ===============

.PHONY: register
# target: register - Register module on PyPi
register:
	@$(VIRTUALENV)/bin/python setup.py register

.PHONY: upload
# target: upload - Upload module on PyPi
upload: clean
	@pip install twine wheel
	@python setup.py sdist upload
	@python setup.py bdist_wheel upload

# =============
#  Development
# =============
#
$(VIRTUALENV):
	@[ -d $(VIRTUALENV) ]	|| virtualenv --no-site-packages $(VIRTUALENV)
	@touch $(VIRTUALENV)

$(VIRTUALENV)/bin/py.test: $(VIRTUALENV) requirements-test.txt
	@$(VIRTUALENV)/bin/pip install -r requirements-test.txt
	@touch $(VIRTUALENV)/bin/py.test

.PHONY: t
# target: t - Runs tests
t: $(VIRTUALENV)/bin/py.test
	@$(VIRTUALENV)/bin/py.test -xs tests

.PHONY: docs
# target: docs - Compile docs
docs:
	@$(VIRTUALENV)/bin/pip install sphinx
	python setup.py build_sphinx --source-dir=docs/ --build-dir=docs/_build --all-files
