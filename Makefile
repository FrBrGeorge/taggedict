MODULE = taggedict
TESTFLAGS = -v
COVERFLAGS = --cov=$(MODULE) --cov-report=html --cov-report=term

all:	check style package

style:
	flake8 $(MODULE)
	pydocstyle $(MODULE)

package:
	python3 -m build


check:
	python -m pytest $(TESTFLAGS)

coverage:
	$(MAKE) TESTFLAGS="$(TESTFLAGS) $(COVERFLAGS)" check

clean:

gitclean:	clean
	git clean -fdx
