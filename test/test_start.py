from start import halbiere


def test_halbiere() -> None:
    assert 1.5 == halbiere(3)
    assert 2.0 == halbiere(4)