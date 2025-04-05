.PHONY: test environment

test:
	python -m unittest

environment:
	micromamba env export --from-history > environment.yaml
	sed -i '/^prefix:/d' environment.yaml