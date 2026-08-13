# BioSequence Visualizer 🧬📊

An Object-Oriented Python application built with **Biopython** and **Matplotlib** to analyze DNA sequences and visualize nucleotide distributions and GC/AT ratios.

## Features

- 🏗️ **Object-Oriented Design (`BioSequence` class)**: Encapsulates sequence attributes, analysis metrics, and plotting tools.
- 🧬 **Biopython Integration**: Uses `Bio.Seq.Seq` and `gc_fraction` for sequence analysis, base counting, and reverse complementation.
- 📊 **Matplotlib Visualizations**:
  - **Bar Chart**: Visualizes individual nucleotide counts (A, T, G, C).
  - **Pie Chart**: Displays exact percentage breakdown of GC vs AT content.
- ⚠️ **Sequence Validation**: Validates DNA input and catches empty strings or non-DNA bases.

## Example Usage

```python
from biosequence import BioSequence

# Create a BioSequence object
sample = BioSequence("AGCTAATTGGCA", name="Test Gene 1")

# Display summary text report
sample.summary()

# Plot nucleotide frequency distribution bar chart
sample.plot_distribution()

# Plot GC vs AT composition pie chart
sample.plot_gc_at_ratio()
```

## Output Example

```text
====Sequence Summary====
Sequence name      : Test Gene 1
Sequence Length    : 12 bp
GC Content         : 41.67%
AT Content         : 58.33%
Base Counts        : {'A': 4, 'T': 3, 'G': 3, 'C': 2}
Reverse Complement : TGCCAATTAGCT
==================================
```

## Technologies Used

- **Python 3**
- **Biopython** (`Bio.Seq`, `Bio.SeqUtils`)
- **Matplotlib** (`pyplot`)

## Run it yourself

```bash
git clone https://github.com/harshwardhan-bio/bioinformatics-projects
cd bioinformatics-projects/biosequence-visualizer
python biosequence.py
```
