.PHONY: help install test lint format clean run-cli run-api

help:
	@echo "Available commands:"
	@echo "  make install    - Install dependencies"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Run linter"
	@echo "  make format     - Format code with black"
	@echo "  make clean      - Clean build artifacts"
	@echo "  make run-cli    - Run CLI example"
	@echo "  make run-api    - Run API server"

install:
	pip install -r requirements.txt
	pip install -e .

test:
	pytest -v --cov=practice --cov-report=term --cov-report=html

lint:
	flake8 src/ tests/
	black --check src/ tests/

format:
	black src/ tests/

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf *.egg-info
	rm -rf build dist

run-cli:
	practice-cli add 10 5

run-api:
	python -m practice.api
