"""Tests for the utils module."""

import pytest
import json
import tempfile
import os
from datetime import datetime
from practice.utils import (
    format_timestamp,
    load_json_file,
    save_json_file,
    validate_number,
    list_operations,
)


class TestFormatTimestamp:
    """Test cases for format_timestamp function."""

    def test_format_with_datetime(self):
        """Test formatting with provided datetime."""
        dt = datetime(2024, 1, 1, 12, 0, 0)
        result = format_timestamp(dt)
        assert "2024-01-01" in result
        assert "12:00:00" in result

    def test_format_without_datetime(self):
        """Test formatting without provided datetime (uses current time)."""
        result = format_timestamp()
        assert isinstance(result, str)
        assert len(result) > 0


class TestJsonFileOperations:
    """Test cases for JSON file operations."""

    def test_save_and_load_json(self):
        """Test saving and loading JSON files."""
        data = {"key": "value", "number": 42}

        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".json") as f:
            filepath = f.name

        try:
            save_json_file(filepath, data)
            loaded_data = load_json_file(filepath)
            assert loaded_data == data
        finally:
            os.unlink(filepath)

    def test_load_nonexistent_file(self):
        """Test loading non-existent file raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError):
            load_json_file("/nonexistent/file.json")

    def test_load_invalid_json(self):
        """Test loading invalid JSON raises JSONDecodeError."""
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".json") as f:
            f.write("invalid json content")
            filepath = f.name

        try:
            with pytest.raises(json.JSONDecodeError):
                load_json_file(filepath)
        finally:
            os.unlink(filepath)


class TestValidateNumber:
    """Test cases for validate_number function."""

    def test_validate_integer(self):
        """Test validating integer."""
        assert validate_number(42) == 42.0

    def test_validate_float(self):
        """Test validating float."""
        assert validate_number(3.14) == 3.14

    def test_validate_string_number(self):
        """Test validating string representation of number."""
        assert validate_number("42") == 42.0
        assert validate_number("3.14") == 3.14

    def test_validate_invalid_value(self):
        """Test validating invalid value raises ValueError."""
        with pytest.raises(ValueError, match="Invalid number"):
            validate_number("not a number")

    def test_validate_none(self):
        """Test validating None raises ValueError."""
        with pytest.raises(ValueError, match="Invalid number"):
            validate_number(None)


class TestListOperations:
    """Test cases for list_operations function."""

    def test_list_operations(self):
        """Test that list_operations returns expected operations."""
        operations = list_operations()
        assert isinstance(operations, list)
        assert "add" in operations
        assert "subtract" in operations
        assert "multiply" in operations
        assert "divide" in operations
        assert "power" in operations
