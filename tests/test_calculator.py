"""Tests for the calculator module."""

import pytest
from practice.calculator import Calculator, calculate


class TestCalculator:
    """Test cases for Calculator class."""

    def test_add(self):
        """Test addition operation."""
        calc = Calculator()
        assert calc.add(2, 3) == 5
        assert calc.add(-1, 1) == 0
        assert calc.add(0, 0) == 0

    def test_subtract(self):
        """Test subtraction operation."""
        calc = Calculator()
        assert calc.subtract(5, 3) == 2
        assert calc.subtract(3, 5) == -2
        assert calc.subtract(0, 0) == 0

    def test_multiply(self):
        """Test multiplication operation."""
        calc = Calculator()
        assert calc.multiply(2, 3) == 6
        assert calc.multiply(-2, 3) == -6
        assert calc.multiply(0, 5) == 0

    def test_divide(self):
        """Test division operation."""
        calc = Calculator()
        assert calc.divide(6, 2) == 3
        assert calc.divide(5, 2) == 2.5
        assert calc.divide(-6, 2) == -3

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        calc = Calculator()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(5, 0)

    def test_power(self):
        """Test power operation."""
        calc = Calculator()
        assert calc.power(2, 3) == 8
        assert calc.power(5, 0) == 1
        assert calc.power(10, 2) == 100


class TestCalculateFunction:
    """Test cases for calculate function."""

    def test_calculate_add(self):
        """Test calculate with add operation."""
        assert calculate("add", 2, 3) == 5

    def test_calculate_subtract(self):
        """Test calculate with subtract operation."""
        assert calculate("subtract", 5, 3) == 2

    def test_calculate_multiply(self):
        """Test calculate with multiply operation."""
        assert calculate("multiply", 4, 5) == 20

    def test_calculate_divide(self):
        """Test calculate with divide operation."""
        assert calculate("divide", 10, 2) == 5

    def test_calculate_power(self):
        """Test calculate with power operation."""
        assert calculate("power", 2, 3) == 8

    def test_calculate_invalid_operation(self):
        """Test calculate with invalid operation."""
        with pytest.raises(ValueError, match="Unsupported operation"):
            calculate("invalid", 1, 2)
