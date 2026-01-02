"""Configuration file for pytest."""

import sys
import os

# Add src directory to path so tests can import the practice module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
