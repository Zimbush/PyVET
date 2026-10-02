from math import comb

def anzahl_lotto_kombinationen(n: int = 49, k: int = 6) -> int:
    """
    Berechnet die Anzahl der möglichen Kombinationen für das deutsche Lotto 6 aus 49.
    Formel: n! / (k! * (n-k)!)
    """
    return comb(n, k)

def produkt(von: int, bis: int) -> int:
    ergebnis = 1
    for faktor in range(von, bis + 1):
        ergebnis *= faktor
    return ergebnis

def kombi() -> int:
    return produkt(44, 49) // produkt(1, 6)
