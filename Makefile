MODULE = tagged
TESTFLAGS = --cov=$(MODULE)

check:
	python -m pytest $(TESTFLAGS)

gitclean:	clean
	git clean -fdx
