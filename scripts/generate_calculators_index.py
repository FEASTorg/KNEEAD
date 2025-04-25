# scripts/generate_calculators_index.py

from pathlib import Path

calc_root = Path("calculators")
output_md = Path("docs/calculators_index.md")

# deep-link into the Lab UI via ?path=…
jupyterlite_base = "lite/lab/index.html?path="

with output_md.open("w", encoding="utf-8") as f:
    f.write("# 📟 Calculator Index\n\n")
    f.write("Click to open each notebook in JupyterLab:\n\n")

    for ipynb in sorted(calc_root.rglob("*.ipynb")):
        if "__pycache__" in ipynb.parts or "shared" in ipynb.parts:
            continue

        # human-friendly title
        name = ipynb.stem.replace("_", " ").title()
        # path *inside* calculators/ → relative to the root of the file-browser
        rel = ipynb.relative_to(calc_root).as_posix()
        # build the URL exactly like Lab’s “Shareable Link”
        url = f"./{jupyterlite_base}{rel}"
        f.write(f"- [{name}]({url})\n")
