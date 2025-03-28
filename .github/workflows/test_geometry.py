import pytest
from geometry import calculate_area

def test_calculate_rectangle_area():
    assert calculate_area("rectangle", width=5, height=4) == 20

def test_calculate_circle_area():
    assert round(calculate_area("circle", radius=3), 2) == 28.27

def test_invalid_shape():
    with pytest.raises(ValueError):
        calculate_area("triangle", base=5, height=10)
