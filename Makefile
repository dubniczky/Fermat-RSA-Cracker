.PHONY: lint test

lint:
	pylint ./src/rsacracker

test:
	python test.py