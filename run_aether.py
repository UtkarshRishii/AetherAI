#!/usr/bin/env python3
import sys
import os

# Ensure the root directory is in the PYTHONPATH so imports work correctly
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from core.main import main

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nShutdown requested by user.")
        sys.exit(0)
