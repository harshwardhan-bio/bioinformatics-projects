def dna_sequence_analyzer(dna_sequence):
    DNA_sequence = dna_sequence.upper()
    right_bases = {"A", "T", "G", "C"}
    complementary_bases = {"A": "T", "T": "A", "G": "C", "C": "G"}
    len1 = len(DNA_sequence)

    if len1 == 0:
        return "The DNA sequence is empty. Please enter a valid DNA sequence."
    else:
        try:
            for base in DNA_sequence:
                if base not in right_bases:
                    raise ValueError(f"Invalid base '{base}' found in the DNA sequence.")

            count_A = DNA_sequence.count("A")
            count_T = DNA_sequence.count("T")
            count_C = DNA_sequence.count("C")
            count_G = DNA_sequence.count("G")

            gc_content = ((count_G + count_C) / len1) * 100
            at_content = 100 - gc_content

            if gc_content > 60:
                gc_category = "High GC content"
            elif 40 <= gc_content <= 60:
                gc_category = "Moderate GC content"
            else:
                gc_category = "Low GC content"

            complementary_sequence = "".join(complementary_bases[base] for base in DNA_sequence)
            reverse_sequence = complementary_sequence[::-1]

            report = (
                "=== DNA Sequence Analysis Report ===\n"
                f"DNA Sequence        : {DNA_sequence}\n"
                f"Sequence Length     : {len1} bp\n"
                f"Base Counts         : A: {count_A}, T: {count_T}, C: {count_C}, G: {count_G}\n"
                f"GC Content         : {gc_content:.2f}%\n"
                f"AT Content         : {at_content:.2f}%\n"
                f"GC Category        : {gc_category}\n"
                f"Complement         : {complementary_sequence}\n"
                f"Reverse Complement  : {reverse_sequence}\n"
                "===================================="
            )
            return report

        except ValueError as e:
            return f"Error: {e} Please enter a valid DNA sequence containing only A, T, G, and C."


if __name__ == "__main__":
    user_seq = input("Enter a DNA sequence: ").strip()
    if user_seq:
        print(dna_sequence_analyzer(user_seq))
    else:
        print(dna_sequence_analyzer("ATGCATGCATGC"))
