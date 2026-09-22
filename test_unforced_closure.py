from verify_unforced_closure import (
    check_exact_arithmetic,
    check_contraction_arithmetic,
    check_lean_source_hygiene,
)

def test_exact_arithmetic():
    check_exact_arithmetic()

def test_contraction_arithmetic():
    check_contraction_arithmetic()

def test_lean_source_hygiene():
    check_lean_source_hygiene()
