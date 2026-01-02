# Practice Repository

A practice repository for testing GitHub automations and agent workflows. This repository provides a simple but complete Python project with predictable structure for experimentation.

## 🎯 Purpose

This repository serves as a safe playground for:
- Testing GitHub automation workflows
- Practicing agent interactions with repositories
- Experimenting with CI/CD pipelines
- Learning code review and testing processes
- Trying out different development workflows

## 📁 Project Structure

```
practice/
├── src/practice/          # Main application code
│   ├── calculator.py      # Calculator logic
│   ├── cli.py             # Command-line interface
│   ├── api.py             # Flask REST API
│   └── utils.py           # Utility functions
├── tests/                 # Test suite
│   ├── test_calculator.py
│   ├── test_api.py
│   └── test_utils.py
├── data/                  # Sample data files
│   ├── config.json
│   └── sample_calculations.json
├── docs/                  # Documentation
│   ├── API.md
│   ├── CLI.md
│   └── DEVELOPMENT.md
├── .github/workflows/     # GitHub Actions workflows
│   ├── ci.yml
│   └── greetings.yml
└── requirements.txt       # Python dependencies
```

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/research-developer/practice.git
cd practice

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -e .
```

### Usage

**CLI:**
```bash
practice-cli add 5 3
practice-cli multiply 4 7 --verbose
```

**API:**
```bash
python -m practice.api
# Visit http://localhost:5000
```

**Tests:**
```bash
pytest
pytest --cov=practice
```

## 🧪 Features

### Calculator Application
- Basic arithmetic operations (add, subtract, multiply, divide, power)
- Command-line interface
- REST API with Flask
- Comprehensive test suite

### Development Tools
- Pytest for testing
- Black for code formatting
- Flake8 for linting
- GitHub Actions for CI/CD

### Sample Data
- JSON configuration files
- Sample calculation data
- Example API responses

## 🤖 Practice Scenarios

This repository is ideal for practicing:

1. **Code Changes**
   - Add new calculator operations
   - Extend the API with new endpoints
   - Refactor existing code

2. **Testing**
   - Write new test cases
   - Improve test coverage
   - Fix failing tests

3. **Documentation**
   - Update API documentation
   - Add code comments
   - Create tutorials

4. **CI/CD**
   - Modify GitHub Actions workflows
   - Add new automation tasks
   - Configure deployment pipelines

5. **Code Review**
   - Create pull requests
   - Review code changes
   - Address feedback

6. **Issue Management**
   - Create and track issues
   - Label and organize work
   - Link PRs to issues

## 📚 Documentation

- [API Documentation](docs/API.md)
- [CLI Documentation](docs/CLI.md)
- [Development Guide](docs/DEVELOPMENT.md)

## 🧰 Commands Cheat Sheet

```bash
# Run tests
pytest
pytest -v
pytest --cov=practice --cov-report=html

# Code quality
black src/ tests/
flake8 src/ tests/

# Run CLI
practice-cli add 10 5
practice-cli divide 20 4 --verbose

# Run API server
python -m practice.api
```

## 🔄 CI/CD

This repository includes GitHub Actions workflows:

- **CI Pipeline** (`ci.yml`): Runs tests and linting on multiple Python versions
- **Greetings** (`greetings.yml`): Welcomes first-time contributors

## 🤝 Contributing

This is a practice repository - feel free to experiment! Create issues, open pull requests, and try different workflows.

## 📝 License

This is a practice repository for educational purposes.

## 🎓 Learning Resources

Use this repository to practice:
- Git workflows (branching, merging, rebasing)
- GitHub features (issues, PRs, actions)
- Python development (testing, packaging, documentation)
- API development (REST endpoints, error handling)
- CLI development (argument parsing, user interaction)
