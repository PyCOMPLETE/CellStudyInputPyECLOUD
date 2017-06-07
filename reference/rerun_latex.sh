#!/bin/bash
set -e

logfile="$1"
PDF_LATEX="$2"
BIBTEX="$3"

i=1
cont=1
while [[ $i -lt 5 ]] && [[ $cont -eq 1 ]] ; do
	cont=0

	if grep -q 'Citation .* undefined' $logfile ; then
		eval $BIBTEX
		eval $PDF_LATEX
		cont=1
		((i++))
	fi

	if grep -q 'Rerun to get ' ${logfile} || grep -q 'undefined references' $logfile; then
		eval $PDF_LATEX
		cont=1
		((i++))
	fi
done

echo "pdflatex or bibtex ran $i times"
