import sys
from pathlib import Path

# Ensure the package root (project dir) is on sys.path when running tests
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
