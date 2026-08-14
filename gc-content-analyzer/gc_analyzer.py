"""
GC Content Analyzer
--------------------
Takes a DNA sequence as input, validates that it only contains real
DNA bases (A, T, G, C), then calculates and classifies its GC content.
"""

def gc_content_analyzer(dna_sequence):
    right_bases = {"A", "T", "G", "C"}
    dna_sequence = dna_sequence.upper()
    len1 = len(dna_sequence)
    if len1 == 0:
        return "The DNA sequence is empty. Please enter a valid DNA sequence."
    else:
        try:
            for base in dna_sequence:
                if base not in right_bases:
                    raise ValueError(f"Invalid base '{base}' found in the DNA sequence.")

            count_C = dna_sequence.count("C")
            count_G = dna_sequence.count("G")
            gc_content = ((count_G + count_C) / len1) * 100

            if gc_content > 60:
                return f"High GC content: {gc_content:.2f}%"
            elif 40 <= gc_content <= 60:
                return f"Moderate GC content: {gc_content:.2f}%"
            else:
                return f"Low GC content: {gc_content:.2f}%"
        except ValueError as e:
            return f"Error: {e} Please enter a valid DNA sequence containing only A, T, G, and C."

if __name__ == "__main__":
    seq = input("Enter a DNA sequence: ").strip()
    result = gc_content_analyzer(seq)
    print(result)
