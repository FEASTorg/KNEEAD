#!/usr/bin/env python3
"""
Generate calculator and page indexes.
Run automatically via pre-commit hook or manually: python scripts/generate_indexes.py
"""

import subprocess
from pathlib import Path

# Run both index generators
scripts_dir = Path(__file__).parent

exec(open(scripts_dir / "generate_calculators_index.py", encoding="utf-8").read())
exec(open(scripts_dir / "generate_pages_index.py", encoding="utf-8").read())

# Stage the generated files if they changed
subprocess.run(
    ["git", "add", "docs/calculators_index.md", "docs/pages_index.md"], check=False
)
