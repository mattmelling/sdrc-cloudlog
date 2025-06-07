.PHONY: mypy
mypy:
	mypy --disable-error-code=import-untyped -p sdrc_cloudlog

.PHONY: ruff
ruff:
	ruff check

.PHONY: lint
lint: mypy ruff
