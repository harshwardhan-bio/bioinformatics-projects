from matplotlib import pyplot as plt
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

class BioSequence:
    def __init__(self, sequence_str, name="Unknown Sequence"):
        self.seq = Seq(sequence_str.strip().upper())
        self.name = name
        self.length = len(self.seq)

        self._validate()
        self.analysis()

    def _validate(self):
        if self.length == 0:
            raise ValueError("Sequence cannot be empty.")
        valid_bases = {"A", "T", "G", "C"}
        for base in self.seq:
            if base not in valid_bases:
                raise ValueError(f"Invalid base '{base}' found in sequence.")

    def analysis(self):
        self.gc_content = gc_fraction(self.seq)*100
        self.at_content = 100 - self.gc_content
        self.dna_count = {
            "A": self.seq.count("A"),
            "T": self.seq.count("T"),
            "G": self.seq.count("G"),
            "C": self.seq.count("C")
        }
        self.reverse_complement = self.seq.reverse_complement()

    def summary(self):
        print("====Sequence Summary====")
        print(f"Sequence name      : {self.name}")
        print(f"Sequence Length    : {self.length} bp")
        print(f"GC Content         : {self.gc_content:.2f}%")
        print(f"AT Content         : {self.at_content:.2f}%")
        print(f"Base Counts        : {self.dna_count}")
        print(f"Reverse Complement : {self.reverse_complement}")
        print("=" * (23 + len(self.name)))

    def plot_distribution(self):
        self.bases = ["A", "T", "G", "C"]
        self.count = self.dna_count.values()
        self.plot = plt.bar(self.bases, self.count)
        plt.title(f"Nucleotide Distribution - {self.name}")
        plt.xlabel("Nucleotide")
        plt.ylabel("Count")
        plt.show()

    def plot_gc_at_ratio(self):
        labels = ["GC Content", "AT Content"]
        ratios = [self.gc_content, self.at_content]
        self.plot = plt.pie(ratios, labels=labels, autopct='%1.1f%%')
        plt.title(f"GC / AT Ratio - {self.name}")
        plt.show()

if __name__ == "__main__":
    seq_input = input("Enter DNA sequence: ").strip()
    if seq_input:
        dna = BioSequence(seq_input)
        dna.summary()
        dna.plot_distribution()
        dna.plot_gc_at_ratio()
