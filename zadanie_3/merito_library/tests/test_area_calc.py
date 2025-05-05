import pytest 
from src.merito_library.area_calc import circle_area, rectangle_area, triangle_area, square_area, trapezoid_area, rhombus_area

def test_circle_area():
    assert circle_area(1) == pytest.approx(3.14159, rel=1e-5)
    assert circle_area(0) == 0
    with pytest.raises(ValueError):
        circle_area(-1)
    with pytest.raises(TypeError):
        circle_area("a")
    assert circle_area(2.5) == pytest.approx(19.63495, rel=1e-5)

def test_rectangle_area():
    assert rectangle_area(10,10) == 100
    assert rectangle_area(0, 5) == 0
    assert rectangle_area(5, 0) == 0
    assert rectangle_area(5, 5) == 25
    with pytest.raises(ValueError):
        rectangle_area(-1, 5)
    with pytest.raises(ValueError):
        rectangle_area(5, -1)
    with pytest.raises(TypeError):
        rectangle_area("a", 5)
    with pytest.raises(TypeError):
        rectangle_area(5, "b")
    assert rectangle_area(2.5, 4) == 10

def test_triangle_area():
    assert triangle_area(10, 5) == 25
    assert triangle_area(0, 5) == 0
    assert triangle_area(5, 0) == 0
    assert triangle_area(5, 5) == 12.5
    with pytest.raises(ValueError):
        triangle_area(-1, 5)
    with pytest.raises(ValueError):
        triangle_area(5, -1)
    with pytest.raises(TypeError):
        triangle_area("a", 5)
    with pytest.raises(TypeError):
        triangle_area(5, "b")
    assert triangle_area(2.5, 4) == 5

def test_square_area():
    assert square_area(10) == 100
    assert square_area(0) == 0
    with pytest.raises(ValueError):
        square_area(-1)
    with pytest.raises(TypeError):
        square_area("a")
    assert square_area(2.5) == 6.25

def test_trapezoid_area():
    assert trapezoid_area(10, 5, 5) == 37.5
    assert trapezoid_area(0, 5, 5) == 12.5
    assert trapezoid_area(5, 5, 5) == 25
    with pytest.raises(ValueError):
        trapezoid_area(-1, 5, 5)
    with pytest.raises(ValueError):
        trapezoid_area(5, -1, 5)
    with pytest.raises(ValueError):
        trapezoid_area(5, 5, -1)
    with pytest.raises(TypeError):
        trapezoid_area("a", 5, 5)
    with pytest.raises(TypeError):
        trapezoid_area(5, "b", 5)
    with pytest.raises(TypeError):
        trapezoid_area(5, 5, "c")
    assert trapezoid_area(2.5, 4, 3) == 9.75

def test_rhombus_area():
    assert rhombus_area(10, 5) == 25
    assert rhombus_area(0, 5) == 0
    assert rhombus_area(5, 0) == 0
    assert rhombus_area(5, 5) == 12.5
    with pytest.raises(ValueError):
        rhombus_area(-1, 5)
    with pytest.raises(ValueError):
        rhombus_area(5, -1)
    with pytest.raises(TypeError):
        rhombus_area("a", 5)
    with pytest.raises(TypeError):
        rhombus_area(5, "b")
    assert rhombus_area(2.5, 4) == 5