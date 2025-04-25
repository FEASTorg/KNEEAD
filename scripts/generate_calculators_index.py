# generate_calculators_index.py

from pathlib import Path

# Where your calculators live on disk…
calc_root = Path("calculators")
# Where to write the markdown index…
output_md = Path("docs/calculators_index.md")
# Lab “tree” deep‐link base
jupyterlite_base = "lite/lab/tree/calculators/"

with output_md.open("w", encoding="utf-8") as f:
    f.write("# 📟 Calculator Index\n\n")
    f.write("Click to open each notebook in JupyterLab:\n\n")

    for ipynb in sorted(calc_root.rglob("*.ipynb")):
        # skip caches or shared utils
        if "__pycache__" in ipynb.parts or "shared" in ipynb.parts:
            continue

        # nice display name
        name = ipynb.stem.replace("_", " ").title()
        # path under calculators/
        rel = ipynb.relative_to(calc_root).as_posix()
        # deep‐link into Lab’s tree view
        url = f"./{jupyterlite_base}{rel}"
        f.write(f"- [{name}]({url})\n")
