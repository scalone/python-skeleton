
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

test: clean-pyc
	SKELETON_ENV=test nosetests

.PHONY: clean-pyc
