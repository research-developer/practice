"""Command-line interface for the practice project."""

import sys
import argparse
from practice.calculator import Calculator
from practice.utils import list_operations


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Practice Calculator CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  practice-cli add 5 3
  practice-cli multiply 4 7
  practice-cli divide 10 2
        """,
    )

    parser.add_argument("operation", choices=list_operations(), help="Operation to perform")
    parser.add_argument("a", type=float, help="First operand")
    parser.add_argument("b", type=float, help="Second operand")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()

    calc = Calculator()

    try:
        if args.operation == "add":
            result = calc.add(args.a, args.b)
        elif args.operation == "subtract":
            result = calc.subtract(args.a, args.b)
        elif args.operation == "multiply":
            result = calc.multiply(args.a, args.b)
        elif args.operation == "divide":
            result = calc.divide(args.a, args.b)
        elif args.operation == "power":
            result = calc.power(args.a, args.b)
        else:
            print(f"Error: Unknown operation '{args.operation}'", file=sys.stderr)
            return 1

        if args.verbose:
            print(f"{args.a} {args.operation} {args.b} = {result}")
        else:
            print(result)

        return 0

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
