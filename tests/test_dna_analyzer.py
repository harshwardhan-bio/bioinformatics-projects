"""
Tests for the DNA Sequence Analyzer.

Run with: python -m pytest tests/test_dna_analyzer.py -v
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "dna-sequence-analyzer"))

from analyzer import dna_sequence_analyzer


def test_valid_sequence_report():
    """A valid sequence should return a complete analysis report."""
    result = dna_sequence_analyzer("ATGCATGCATGC")
    assert "=== DNA Sequence Analysis Report ===" in result
    assert "A: 3" in result
    assert "T: 3" in result
    assert "G: 3" in result
    assert "C: 3" in result


def test_gc_content_calculation():
    """GC content for ATGCATGCATGC (50% GC) should be 50.00%."""
    result = dna_sequence_analyzer("ATGCATGCATGC")
    assert "50.00%" in result
    assert "Moderate" in result


def test_complement_generation():
    """Complement of ATGC should be TACG."""
    result = dna_sequence_analyzer("ATGC")
    assert "TACG" in result


def test_reverse_complement():
    """Reverse complement of ATGC should be GCAT."""
    result = dna_sequence_analyzer("ATGC")
    assert "GCAT" in result


def test_empty_sequence():
    """An empty string should return an error message."""
    result = dna_sequence_analyzer("")
    assert "empty" in result.lower()


def test_invalid_base():
    """A sequence with non-DNA characters should return an error."""
    result = dna_sequence_analyzer("ATGCXYZ")
    assert "Error" in result
    assert "X" in result


def test_lowercase_input():
    """Lowercase input should be normalized and analyzed correctly."""
    result = dna_sequence_analyzer("atgc")
    assert "ATGC" in result
    assert "TACG" in result


def test_high_gc_classification():
    """A GC-rich sequence should be classified as High."""
    result = dna_sequence_analyzer("GCGCGCGCGC")
    assert "High" in result


def test_low_gc_classification():
    """An AT-rich sequence should be classified as Low."""
    result = dna_sequence_analyzer("AATTAATTAA")
    assert "Low" in result
