# CLI Documentation

## Overview

The Practice CLI provides a command-line interface for performing arithmetic calculations.

## Installation

```bash
pip install -e .
```

## Usage

```bash
practice-cli OPERATION A B [OPTIONS]
```

### Arguments

- `OPERATION`: The operation to perform (add, subtract, multiply, divide, power)
- `A`: First operand (number)
- `B`: Second operand (number)

### Options

- `-v, --verbose`: Enable verbose output
- `-h, --help`: Show help message

## Examples

### Basic Usage

```bash
# Add two numbers
practice-cli add 5 3
# Output: 8.0

# Multiply two numbers
practice-cli multiply 4 7
# Output: 28.0

# Divide two numbers
practice-cli divide 10 2
# Output: 5.0
```

### Verbose Output

```bash
practice-cli add 5 3 --verbose
# Output: 5.0 add 3.0 = 8.0
```

### Floating Point Numbers

```bash
practice-cli add 3.14 2.86
# Output: 6.0

practice-cli divide 22 7
# Output: 3.142857142857143
```

### Power Operation

```bash
practice-cli power 2 8
# Output: 256.0
```

## Error Handling

### Division by Zero

```bash
practice-cli divide 10 0
# Error: Cannot divide by zero
```

### Invalid Input

```bash
practice-cli add invalid 5
# usage: practice-cli [-h] [-v] {add,subtract,multiply,divide,power} a b
# practice-cli: error: argument a: invalid float value: 'invalid'
```
