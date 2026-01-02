# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-01-02

### Added
- Initial project structure with Python package
- Calculator module with basic arithmetic operations (add, subtract, multiply, divide, power)
- Command-line interface for calculator
- Flask REST API with endpoints:
  - GET / - API information
  - GET /health - Health check
  - POST /calculate - Perform calculations
  - GET /operations - List available operations
- Comprehensive test suite with pytest
  - Calculator tests
  - API tests
  - Utility function tests
- Development tools and configuration:
  - pytest for testing
  - black for code formatting
  - flake8 for linting
  - Makefile for common tasks
- GitHub Actions workflows:
  - CI pipeline with multi-version Python testing
  - Contributor greeting workflow
- Documentation:
  - API documentation
  - CLI documentation
  - Development guide
  - Practice tasks guide
  - Contributing guidelines
- Sample data files (JSON)
- Issue and PR templates
- MIT License

### Testing
- 31 test cases covering all major functionality
- Code coverage reporting
- Linting and formatting checks

[0.1.0]: https://github.com/research-developer/practice/releases/tag/v0.1.0
