# DNA Sequence Analyzer 🧬

A Python tool that validates a DNA sequence and reports its nucleotide
composition, GC/AT content, complementary strand, and reverse complement.

## What it does

- ✅ Validates that the input contains only real DNA bases (A, T, G, C)
- 🔢 Counts each nucleotide (A, T, G, C)
- 📊 Calculates GC content and AT content, and classifies GC content as
  High / Moderate / Low
- 🔄 Generates the complementary strand (A↔T, G↔C)
- ↩️ Generates the reverse complement — the paired strand written in its
  own correct 5'→3' reading direction

## Why this matters biologically

DNA's two strands are antiparallel — they run in opposite chemical
directions. The plain complement shows which base pairs with which,
but the reverse complement is what the paired strand actually looks
like when written the conventional way every sequence database and
tool (like BLAST) reads it. Because a gene can sit on either strand,
real sequence-search tools check both the original sequence and its
reverse complement — this project reproduces that same logic.

## Example usage

```bash
python analyzer.py
```

## Example output

```text
=== DNA Sequence Analysis Report ===
DNA Sequence        : ATGCATGCATGC
Sequence Length     : 12 bp
Base Counts         : A: 3, T: 3, C: 3, G: 3
GC Content          : 50.00%
AT Content          : 50.00%
GC Category         : Moderate GC content
Complement          : TACGTACGTACG
Reverse Complement : GCATGCATGCAT
====================================
```

## Error handling

Invalid bases are caught before any calculation runs, and the exact
offending character is named:

```text
Enter a DNA sequence: ATGCX
Error: Invalid base 'X' found in the DNA sequence. Please enter a
valid DNA sequence containing only A, T, G, and C.
```

## Technologies used

- Python 3 (standard library only — no external dependencies)

## What I learned building this

Extended a simple GC-content calculator into a fuller sequence analysis
tool — using a dictionary to map complementary bases, a generator
expression with `.join()` to build the complement efficiently, and
string slicing (`[::-1]`) to reverse it. Testing this against a
hand-calculated example (`ATGC` → `TACG` → `GCAT`) before trusting it
on longer sequences was a good habit for catching logic errors early.

## Run it yourself

```bash
git clone https://github.com/harshwardhan-bio/bioinformatics-projects
cd bioinformatics-projects/dna-sequence-analyzer
python analyzer.py
```
