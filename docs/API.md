# API Documentation

## Overview

The Practice API provides a simple REST interface for performing arithmetic calculations.

## Base URL

```
http://localhost:5000
```

## Endpoints

### GET /

Get API information.

**Response:**
```json
{
  "message": "Practice API",
  "version": "0.1.0",
  "timestamp": "2024-01-01T12:00:00.000000"
}
```

### GET /health

Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00.000000"
}
```

### POST /calculate

Perform a calculation.

**Request Body:**
```json
{
  "operation": "add",
  "a": 5,
  "b": 3
}
```

**Operations:** `add`, `subtract`, `multiply`, `divide`, `power`

**Response:**
```json
{
  "operation": "add",
  "operands": {"a": 5, "b": 3},
  "result": 8,
  "timestamp": "2024-01-01T12:00:00.000000"
}
```

**Error Response:**
```json
{
  "error": "Error message"
}
```

### GET /operations

List available operations.

**Response:**
```json
{
  "operations": ["add", "subtract", "multiply", "divide", "power"],
  "timestamp": "2024-01-01T12:00:00.000000"
}
```

## Examples

### Using curl

```bash
# Add two numbers
curl -X POST http://localhost:5000/calculate \
  -H "Content-Type: application/json" \
  -d '{"operation": "add", "a": 10, "b": 5}'

# Divide two numbers
curl -X POST http://localhost:5000/calculate \
  -H "Content-Type: application/json" \
  -d '{"operation": "divide", "a": 20, "b": 4}'
```

### Using Python

```python
import requests

response = requests.post('http://localhost:5000/calculate', json={
    'operation': 'multiply',
    'a': 7,
    'b': 8
})

print(response.json())
# {"operation": "multiply", "operands": {"a": 7, "b": 8}, "result": 56, ...}
```
