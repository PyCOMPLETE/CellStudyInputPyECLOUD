# A useful makefile for latex

#Final name of output
TARGET = photoelectrons_in_PyECLOUD.pdf

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
	plots/energy_distribution_impact.png\
	plots/cosine_power.png\
	plots/study_1.png\
	plots/summed_hl_1.png\
	$(TARGET)

# Makefile Rules
$(TARGET) : $(TEX_FILES) $(PNG_FILES) $(MAIN_BIB)
	$(PDF_LATEX)
	$(RERUN) "$(ROOT).log" "$(PDF_LATEX)" "$(BIBTEX)"
	grep 'Warning' $(ROOT).log || true
	mv $(ROOT).pdf $(TARGET)

#plots/energy_distribution_impact.png: ~/pyecloud/photoelectrons/005_energy_dist.py
#	python2 $< -o $@ --noshow
#	$(TRIM) $@ $@
#
#plots/cosine_power.png: ./scripts/000_cos_sq.py
#	python2 $< -o $@ --noshow
#	$(TRIM) $@ $@
#
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

./plots/study_1.png: ~/pyecloud/cell_scan/005_cell_study.py
	python2 $< -o ./plots/study --noshow
	for ii in ./plots/study*.png ; do $(TRIM) $$ii $$ii ; done

./plots/summed_hl_1.png: ~/pyecloud/cell_scan/001_heat_load_estimate.py
	python2 $< -o ./plots/summed_hl --noshow
	for ii in ./plots/summed_hl*.png ; do $(TRIM) $$ii $$ii ; done

