# GC Content Analyzer 🧬

A Python tool that calculates the GC content of a DNA sequence and
classifies it as High, Moderate, or Low — with input validation to
catch invalid DNA bases before doing any calculation.

## What it does

- ✅ Validates that the input contains only real DNA bases (A, T, G, C)
- 📊 Calculates GC content as a percentage
- 🏷️ Classifies the result:
  - **High** — above 60%
  - **Moderate** — 40–60%
  - **Low** — below 40%
- ⚠️ Reports the exact invalid character if the sequence contains one

## Why GC content matters

G-C base pairs form three hydrogen bonds compared to two for A-T,
so sequences with higher GC content are generally more thermally
stable. This is a real consideration in applications like PCR primer
design, where GC content affects binding strength and melting
temperature.

## Example usage

```bash
python gc_analyzer.py
Enter a DNA sequence: ATGCGATCGATCGGGCCTA
Moderate GC content: 57.89%
```

## Error handling example

```bash
Enter a DNA sequence: ATGCX
Error: Invalid base 'X' found in the DNA sequence. Please enter a
valid DNA sequence containing only A, T, G, and C.
```

## Technologies used

- Python 3 (standard library only — no external dependencies)

## What I learned building this

Started as a basic GC-content calculator and evolved as I learned more
Python — using a `set` for fast base validation, and `try/except` with
a custom error message instead of letting bad input crash the program
or silently produce wrong results.

## Run it yourself

```bash
git clone https://github.com/harshwardhan-bio/bioinformatics-projects
cd bioinformatics-projects/gc-content-analyzer
python gc_analyzer.py
```
