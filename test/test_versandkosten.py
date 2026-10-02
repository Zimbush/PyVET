import pytest
from versandkosten import berechne_versandkosten

def test_bestellsumme():
    assert berechne_versandkosten(37.75) == 4.90
    assert berechne_versandkosten(65.83) == 0.00
    assert berechne_versandkosten(49.99) == 4.90
    assert berechne_versandkosten(50.00) == 0.00


@pytest.mark.parametrize("summe,erwartet", [
    (25.50, 4.90),
    (49.99, 4.90),
    (50.00, 0.00),
    (75.25, 0.00),
])
def test_verschiedene_bestellsummen(summe: float, erwartet: float):
    """Test mit verschiedenen Bestellsummen"""
    assert berechne_versandkosten(summe) == erwartet
