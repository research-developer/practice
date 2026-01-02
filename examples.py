#!/usr/bin/env python3
"""
Example script demonstrating usage of the practice project.

This script shows how to:
- Use the Calculator class
- Make API calls
- Handle errors
"""

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from practice.calculator import Calculator
from practice.utils import list_operations, format_timestamp


def demo_calculator():
    """Demonstrate calculator usage."""
    print("=" * 60)
    print("Calculator Demo")
    print("=" * 60)

    calc = Calculator()

    # Basic operations
    operations = [
        ("add", 10, 5),
        ("subtract", 10, 5),
        ("multiply", 10, 5),
        ("divide", 10, 5),
        ("power", 2, 8),
    ]

    for op_name, a, b in operations:
        if op_name == "add":
            result = calc.add(a, b)
        elif op_name == "subtract":
            result = calc.subtract(a, b)
        elif op_name == "multiply":
            result = calc.multiply(a, b)
        elif op_name == "divide":
            result = calc.divide(a, b)
        elif op_name == "power":
            result = calc.power(a, b)

        print(f"{a} {op_name} {b} = {result}")

    # Error handling
    print("\nError Handling Demo:")
    try:
        calc.divide(10, 0)
    except ValueError as e:
        print(f"Caught error: {e}")


def demo_utils():
    """Demonstrate utility functions."""
    print("\n" + "=" * 60)
    print("Utils Demo")
    print("=" * 60)

    print(f"Available operations: {list_operations()}")
    print(f"Current timestamp: {format_timestamp()}")


def main():
    """Run all demonstrations."""
    print("\n🎯 Practice Project - Examples\n")

    demo_calculator()
    demo_utils()

    print("\n" + "=" * 60)
    print("Demo completed! Try running:")
    print("  - python -m practice.cli add 10 5")
    print("  - python -m practice.api")
    print("  - pytest")
    print("=" * 60)


if __name__ == "__main__":
    main()
