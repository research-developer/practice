# Practice Tasks

This document lists various practice tasks you can attempt in this repository.

## Beginner Tasks

### Task 1: Add a New Calculator Operation
**Difficulty:** ⭐ Easy  
**Objective:** Add a modulo operation to the calculator

**Steps:**
1. Add a `modulo(a, b)` method to the `Calculator` class in `src/practice/calculator.py`
2. Update the `calculate()` function to support "modulo" operation
3. Add test cases in `tests/test_calculator.py`
4. Update CLI to support the new operation
5. Run tests to verify

**Learning Outcomes:** Basic Python, TDD, code structure

### Task 2: Improve Documentation
**Difficulty:** ⭐ Easy  
**Objective:** Add more examples to the documentation

**Steps:**
1. Pick one of the docs files in `docs/`
2. Add more usage examples
3. Add common troubleshooting tips
4. Submit a PR

**Learning Outcomes:** Documentation practices, Git workflow

### Task 3: Add a New API Endpoint
**Difficulty:** ⭐ Easy  
**Objective:** Add a `/history` endpoint to track calculation history

**Steps:**
1. Add a new endpoint in `src/practice/api.py`
2. Store calculation results in memory
3. Return list of recent calculations
4. Add tests in `tests/test_api.py`

**Learning Outcomes:** REST API design, Flask basics

## Intermediate Tasks

### Task 4: Implement Calculation History
**Difficulty:** ⭐⭐ Medium  
**Objective:** Add persistent calculation history using JSON files

**Steps:**
1. Create a `History` class in a new `src/practice/history.py` module
2. Save calculations to `data/history.json`
3. Load and display history
4. Add CLI command to view history
5. Add comprehensive tests

**Learning Outcomes:** File I/O, data persistence, module design

### Task 5: Add Input Validation
**Difficulty:** ⭐⭐ Medium  
**Objective:** Improve error handling and input validation

**Steps:**
1. Add comprehensive input validation
2. Create custom exception classes
3. Add detailed error messages
4. Test edge cases
5. Update documentation

**Learning Outcomes:** Error handling, validation patterns, testing

### Task 6: Implement API Authentication
**Difficulty:** ⭐⭐ Medium  
**Objective:** Add basic API key authentication

**Steps:**
1. Add API key generation
2. Implement authentication decorator
3. Update API endpoints
4. Add authentication tests
5. Document authentication flow

**Learning Outcomes:** Security basics, decorators, API design

## Advanced Tasks

### Task 7: Add Database Support
**Difficulty:** ⭐⭐⭐ Hard  
**Objective:** Replace JSON with SQLite database

**Steps:**
1. Design database schema
2. Add SQLAlchemy or sqlite3 integration
3. Migrate existing data
4. Update all components
5. Add migration scripts
6. Comprehensive testing

**Learning Outcomes:** Database design, ORMs, data migration

### Task 8: Build a Web UI
**Difficulty:** ⭐⭐⭐ Hard  
**Objective:** Create a web interface for the calculator

**Steps:**
1. Add HTML/CSS/JavaScript frontend
2. Connect to the API
3. Implement calculator UI
4. Add history display
5. Make it responsive
6. Deploy

**Learning Outcomes:** Frontend development, full-stack integration

### Task 9: CI/CD Enhancement
**Difficulty:** ⭐⭐⭐ Hard  
**Objective:** Improve CI/CD pipeline

**Steps:**
1. Add deployment workflow
2. Add security scanning
3. Add automated releases
4. Add Docker support
5. Add staging environment
6. Documentation updates

**Learning Outcomes:** DevOps, CI/CD, containerization

## GitHub Automation Practice

### Task 10: Create an Issue Bot
**Difficulty:** ⭐⭐ Medium  
**Objective:** Add a bot that responds to specific issue labels

**Steps:**
1. Create a new workflow in `.github/workflows/`
2. Use GitHub Actions to respond to issues
3. Add automatic labels based on content
4. Test with real issues

**Learning Outcomes:** GitHub Actions, automation

### Task 11: Add Code Review Automation
**Difficulty:** ⭐⭐⭐ Hard  
**Objective:** Automated code review comments

**Steps:**
1. Add linting checks that comment on PRs
2. Add complexity analysis
3. Add test coverage requirements
4. Auto-assign reviewers

**Learning Outcomes:** GitHub Actions, code quality automation

## Tips for Success

- Start with easier tasks and progress gradually
- Read existing code to understand patterns
- Run tests frequently
- Ask questions if stuck
- Have fun and experiment!

## Submitting Your Work

1. Create a new branch for your task
2. Make your changes
3. Run all tests and linting
4. Create a pull request
5. Reference the task number in your PR
