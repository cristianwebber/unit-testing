test:
	python -m pytest -v

coverage:
	python -m coverage run -m pytest
	python -m coverage report -m