"""Utility functions for the practice project."""

import json
from datetime import datetime


def format_timestamp(dt=None):
    """Format a datetime object as ISO 8601 string.

    Args:
        dt: datetime object to format. If None, uses current time.

    Returns:
        ISO 8601 formatted string
    """
    if dt is None:
        dt = datetime.now()
    return dt.isoformat()


def load_json_file(filepath):
    """Load JSON data from a file.

    Args:
        filepath: Path to the JSON file

    Returns:
        Parsed JSON data

    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If file contains invalid JSON
    """
    with open(filepath, "r") as f:
        return json.load(f)


def save_json_file(filepath, data):
    """Save data to a JSON file.

    Args:
        filepath: Path to save the JSON file
        data: Data to serialize to JSON
    """
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)


def validate_number(value):
    """Validate that a value can be converted to a number.

    Args:
        value: Value to validate

    Returns:
        Float representation of the value

    Raises:
        ValueError: If value cannot be converted to a number
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid number: {value}")


def list_operations():
    """Return a list of available calculator operations.

    Returns:
        List of operation names
    """
    return ["add", "subtract", "multiply", "divide", "power"]
