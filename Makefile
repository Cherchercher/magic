init:
	pip install -r requirements.txt
test:
	python tests
.PHONY: init test