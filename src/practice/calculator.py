"""A simple calculator module for basic arithmetic operations."""


class Calculator:
    """Calculator class for performing basic arithmetic operations."""

    def add(self, a, b):
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b
        """
        return a + b

    def subtract(self, a, b):
        """Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b
        """
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b
        """
        return a * b

    def divide(self, a, b):
        """Divide a by b.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Quotient of a and b

        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, base, exponent):
        """Raise base to the power of exponent.

        Args:
            base: Base number
            exponent: Exponent

        Returns:
            base raised to the power of exponent
        """
        return base**exponent


def calculate(operation, a, b):
    """Perform a calculation based on the operation string.

    Args:
        operation: Operation to perform (add, subtract, multiply, divide, power)
        a: First operand
        b: Second operand

    Returns:
        Result of the operation

    Raises:
        ValueError: If operation is not supported
    """
    calc = Calculator()
    operations = {
        "add": calc.add,
        "subtract": calc.subtract,
        "multiply": calc.multiply,
        "divide": calc.divide,
        "power": calc.power,
    }

    if operation not in operations:
        raise ValueError(f"Unsupported operation: {operation}")

    return operations[operation](a, b)
