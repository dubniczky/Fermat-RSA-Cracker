.PHONY: lint test

lint:
	pylint ../rsacracker

test:
	python test.py