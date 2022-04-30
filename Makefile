MODULE = tagged
TESTFLAGS = -v
COVERFLAGS = --cov=$(MODULE) --cov-report=html --cov-report=term

check:
	python -m pytest $(TESTFLAGS)

coverage:
	$(MAKE) TESTFLAGS="$(TESTFLAGS) $(COVERFLAGS)" check


gitclean:	clean
	git clean -fdx
