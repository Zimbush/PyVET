from lotto import anzahl_lotto_kombinationen, kombi, produkt

def test_standard_lotto():
    assert anzahl_lotto_kombinationen() == 13983816

def test_andere_werte():
    assert anzahl_lotto_kombinationen(10, 2) == 45
    assert anzahl_lotto_kombinationen(5, 5) == 1
    assert anzahl_lotto_kombinationen(7, 0) == 1

def test_produkt():
    assert produkt(1, 1) == 1
    assert produkt(1, 6) == 720
    assert produkt(3, 5) == 60


def test_kombi():
    assert kombi() == 13983816
