# A useful makefile for latex

#Title
TITLE = photoelectrons_in_PyECLOUD.pdf

# Config
ROOT = main
MAIN_BIB = lit.bib
PDF_LATEX = pdflatex -halt-on-error -file-line-error $(ROOT).tex
BIBTEX = bibtex $(ROOT).aux
RERUN = ./rerun_latex.sh
TRIM = convert -trim

# Handle epslatex stuff
TEX_FILES = $(wildcard *.tex src/*.tex)
PNG_FILES = $(wildcard plots/*.png)

.PHONY: all
all:\
	plots/test_module.png\
	plots/n_photons.png\
	plots/distributions.png\
	plots/time.png\
	$(TITLE)

# Makefile Rules
$(TITLE) : $(TEX_FILES) $(PNG_FILES) $(MAIN_BIB)
	$(PDF_LATEX)
	$(RERUN) "$(ROOT).log" "$(PDF_LATEX)" "$(BIBTEX)"
	grep 'Warning' $(ROOT).log || true
	mv $(ROOT).pdf $(TITLE)

#plots/n_photons.png: ../001_number_of_photons.py
#	python2 $< -o $@ --noshow
#	$(TRIM) $@ $@
#
#plots/distributions.png: ./scripts/001_distributions.py
#	python2 $< -o $@ --noshow
#	$(TRIM) $@ $@
#
#plots/test_module.png: ~/pythonpath/PyECLOUD/test_photoemission.py
#	python2 $< -o $@ --noshow
#	$(TRIM) $@ $@
#
#plots/time.png: ./scripts/002_kin_energy_time.py
#	python2 $< -o $@ --noshow
#	$(TRIM) $@ $@
