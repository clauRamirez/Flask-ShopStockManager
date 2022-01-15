import unittest
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).absolute().parent.parent
sys.path.insert(0, f"{ROOT_DIR}")

from tests.book_test import TestBook

if __name__ == '__main__':
    unittest.main()
