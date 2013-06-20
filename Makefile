MODULE=dealer
SPHINXBUILD=sphinx-build
ALLSPHINXOPTS= -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
BUILDDIR=_build


.PHONY: help
# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile

.PHONY: clean
# target: clean - Clean repo
clean:
	sudo rm -rf build dist
	find . -name "*.pyc" -delete
	find . -name "*.orig" -delete

.PHONY: register
# target: register - Register module on PyPi
register:
	python setup.py register

.PHONY: upload
# target: upload - Upload module on PyPi
upload: clean
	python setup.py sdist upload || echo 'Upload already'

.PHONY: t
# target: t - Run module tests
t:
	python setup.py test

.PHONY: audit
# target: audit - Audit code
audit:
	pylama $(MODULE) -i E501

.PHONY: travis
# target: travis - Audit code and run tests
travis: audit t

.PHONY: docs
# target: docs - Compile docs
docs:
	python setup.py build_sphinx --source-dir=docs/ --build-dir=docs/_build --all-files
	# python setup.py upload_sphinx --upload-dir=docs/_build/html

.PHONY: pep8
pep8:
	find $(MODULE) -name "*.py" | xargs -n 1 autopep8 -i
