"""Simple module for calculating the area of different shapes."""

import math
from typing import Union


def circle_area(radius: Union[int, float]) -> float:
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * (radius ** 2)


def rectangle_area(
        length: Union[int, float], width: Union[int, float]) -> float:
    """Calculate the area of a rectangle given its length and width."""
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")
    return length * width


def triangle_area(base: Union[int, float], height: Union[int, float]) -> float:
    """Calculate the area of a triangle given its base and height."""
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative.")
    return 0.5 * base * height


def square_area(side: Union[int, float]) -> float:
    """Calculate the area of a square given its side length."""
    if side < 0:
        raise ValueError("Side length cannot be negative.")
    return side ** 2


def trapezoid_area(
    base1: Union[int, float],
    base2: Union[int, float],
    height: Union[int, float]
) -> float:
    """Calculate the area of a trapezoid given its bases and height."""
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("Bases and height cannot be negative.")
    return ((base1 + base2) / 2) * height


def rhombus_area(e: Union[int, float], f: Union[int, float]) -> float:
    """Calculate the area of a rhombus given its diagonals."""
    if e < 0 or f < 0:
        raise ValueError("Diagonals cannot be negative.")
    return (e * f) / 2
