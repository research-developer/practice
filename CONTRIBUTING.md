# Contributing to Practice Repository

Thank you for your interest in contributing! This is a practice repository designed for testing and experimentation.

## Getting Started

1. Fork the repository
2. Clone your fork
3. Create a new branch for your feature or fix
4. Make your changes
5. Run tests and linting
6. Submit a pull request

## Development Setup

```bash
# Install dependencies
pip install -r requirements.txt
pip install -e .

# Run tests
pytest

# Run linting
flake8 src/ tests/
black --check src/ tests/

# Format code
black src/ tests/
```

## Pull Request Guidelines

- Keep changes focused and atomic
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass
- Follow existing code style

## Testing

All code changes should include tests. Run the test suite with:

```bash
pytest
pytest --cov=practice
```

## Code Style

We use:
- **Black** for code formatting
- **Flake8** for linting
- **Pytest** for testing

## Practice Scenarios

Feel free to experiment with:
- Adding new calculator operations
- Creating new API endpoints
- Improving test coverage
- Updating documentation
- Modifying GitHub Actions workflows

## Questions?

This is a practice repository - don't hesitate to experiment and learn!
