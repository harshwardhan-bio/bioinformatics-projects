"""
Tests for the GC Content Analyzer.

Run with: python -m pytest tests/test_gc_analyzer.py -v
"""

import sys
import os

# Add parent directory to path so we can import from project folders
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "gc-content-analyzer"))

from gc_analyzer import gc_content_analyzer


def test_moderate_gc_content():
    """A sequence with ~58% GC should be classified as Moderate."""
    result = gc_content_analyzer("ATGCGATCGATCGGGCCTA")
    assert "Moderate" in result


def test_high_gc_content():
    """A GC-rich sequence (>60%) should be classified as High."""
    result = gc_content_analyzer("GCGCGCGCGC")
    assert "High" in result


def test_low_gc_content():
    """An AT-rich sequence (<40% GC) should be classified as Low."""
    result = gc_content_analyzer("AATTAATTAA")
    assert "Low" in result


def test_empty_sequence():
    """An empty string should return an error message."""
    result = gc_content_analyzer("")
    assert "empty" in result.lower()


def test_invalid_base():
    """A sequence with non-DNA characters should return an error."""
    result = gc_content_analyzer("ATGCX")
    assert "Error" in result


def test_lowercase_input():
    """Lowercase input should be handled correctly."""
    result = gc_content_analyzer("atgcgatcgatcgggccta")
    assert "Moderate" in result


def test_all_gc():
    """A sequence of only G and C should be 100% GC."""
    result = gc_content_analyzer("GGGGCCCC")
    assert "100.00%" in result


def test_all_at():
    """A sequence of only A and T should be 0% GC (Low)."""
    result = gc_content_analyzer("AAAATTTT")
    assert "0.00%" in result
    assert "Low" in result
