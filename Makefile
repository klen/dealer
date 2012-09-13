MODULE=dealer
SPHINXBUILD=sphinx-build
ALLSPHINXOPTS= -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
BUILDDIR=_build


.PHONY: clean
clean:
	sudo rm -rf build dist
	find . -name "*.pyc" -delete
	find . -name "*.orig" -delete

.PHONY: register
register:
	python setup.py register

.PHONY: upload
upload:
	python setup.py sdist upload || echo 'Upload already'

.PHONY: test
test:
	python setup.py test

.PHONY: audit
audit:
	pylama $(MODULE) -i E501

.PHONY: travis
travis: audit test

.PHONY: docs
docs:
	python setup.py build_sphinx --source-dir=docs/ --build-dir=docs/_build --all-files
	python setup.py upload_sphinx --upload-dir=docs/_build/html

.PHONY: pep8
pep8:
	find $(MODULE) -name "*.py" | xargs -n 1 autopep8 -i
