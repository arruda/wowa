.PHONY: clean-pyc docs clean

help:
	@echo "clean - test, coverage and Python artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"

clean: clean-pyc clean-test

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -fr htmlcov/

lint:
	flake8

test:
	wowa/manage.py test

coverage:
	coverage run wowa/manage.py test
	coverage report -m
	coverage html

docs:
	rm -f docs/wowa.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ wowa
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
