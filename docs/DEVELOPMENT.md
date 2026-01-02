# Development Guide

## Setup

1. Clone the repository:
```bash
git clone https://github.com/research-developer/practice.git
cd practice
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
pip install -e .
```

## Running Tests

Run all tests:
```bash
pytest
```

Run with coverage:
```bash
pytest --cov=practice --cov-report=html
```

Run specific test file:
```bash
pytest tests/test_calculator.py
```

## Code Quality

### Linting

Check code style with flake8:
```bash
flake8 src/ tests/
```

### Formatting

Format code with black:
```bash
black src/ tests/
```

Check formatting without making changes:
```bash
black --check src/ tests/
```

## Running the Application

### CLI

```bash
practice-cli add 5 3
```

### API Server

```bash
python -m practice.api
# or
cd src && python -m practice.api
```

The API will be available at `http://localhost:5000`

## Project Structure

```
practice/
├── src/
│   └── practice/
│       ├── __init__.py
│       ├── calculator.py  # Calculator logic
│       ├── cli.py         # CLI interface
│       ├── api.py         # Flask API
│       └── utils.py       # Utility functions
├── tests/
│   ├── conftest.py
│   ├── test_calculator.py
│   ├── test_api.py
│   └── test_utils.py
├── data/
│   ├── config.json
│   └── sample_calculations.json
├── docs/
│   ├── API.md
│   ├── CLI.md
│   └── DEVELOPMENT.md
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```

## Adding New Features

1. Create a new branch
2. Add your feature code
3. Add tests for your feature
4. Run tests and linting
5. Submit a pull request
