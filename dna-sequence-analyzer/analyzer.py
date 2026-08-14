"""
DNA Sequence Analyzer
---------------------
Validates a DNA sequence and reports its nucleotide composition,
GC/AT content, complementary strand, and reverse complement.
"""


def dna_sequence_analyzer(dna_sequence):
    """Analyze a DNA sequence and return a formatted report.

    Validates the input, counts each nucleotide, calculates GC/AT content,
    generates the complementary strand and reverse complement.

    Args:
        dna_sequence: A string containing DNA bases (A, T, G, C).

    Returns:
        A formatted string report, or an error message if input is invalid.
    """
    sequence = dna_sequence.upper()
    valid_bases = {"A", "T", "G", "C"}
    complement_map = {"A": "T", "T": "A", "G": "C", "C": "G"}
    length = len(sequence)

    if length == 0:
        return "The DNA sequence is empty. Please enter a valid DNA sequence."
    else:
        try:
            for base in sequence:
                if base not in valid_bases:
                    raise ValueError(f"Invalid base '{base}' found in the DNA sequence.")

            count_A = sequence.count("A")
            count_T = sequence.count("T")
            count_C = sequence.count("C")
            count_G = sequence.count("G")

            gc_content = ((count_G + count_C) / length) * 100
            at_content = 100 - gc_content

            if gc_content > 60:
                gc_category = "High GC content"
            elif 40 <= gc_content <= 60:
                gc_category = "Moderate GC content"
            else:
                gc_category = "Low GC content"

            complement = "".join(complement_map[base] for base in sequence)
            reverse_complement = complement[::-1]

            report = (
                "=== DNA Sequence Analysis Report ===\n"
                f"DNA Sequence        : {sequence}\n"
                f"Sequence Length     : {length} bp\n"
                f"Base Counts         : A: {count_A}, T: {count_T}, C: {count_C}, G: {count_G}\n"
                f"GC Content         : {gc_content:.2f}%\n"
                f"AT Content         : {at_content:.2f}%\n"
                f"GC Category        : {gc_category}\n"
                f"Complement         : {complement}\n"
                f"Reverse Complement  : {reverse_complement}\n"
                "===================================="
            )
            return report

        except ValueError as e:
            return f"Error: {e} Please enter a valid DNA sequence containing only A, T, G, and C."


if __name__ == "__main__":
    seq = input("Enter a DNA sequence: ").strip()
    print(dna_sequence_analyzer(seq))
