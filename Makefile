# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = build
MODULE = taggedict
TESTFLAGS = -v
COVERFLAGS = --cov=$(MODULE) --cov-report=html --cov-report=term

all:	check style package

style:
	flake8 $(MODULE)
	pydocstyle $(MODULE)

package:
	python -m build

publish:	clean package
	python3 -m twine upload --repository testpypi dist/*

check:
	python -m pytest $(TESTFLAGS)

coverage:
	$(MAKE) TESTFLAGS="$(TESTFLAGS) $(COVERFLAGS)" check

clean:
	rm -rf dist

gitclean:	clean
	git clean -fdx

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
