# generate_calculators_index.py

from pathlib import Path

calc_root = Path("calculators")
output_md = Path("docs/calculators_index.md")
jupyterlite_base_url = "lite/lab/index.html?path="

with output_md.open("w", encoding="utf-8") as f:
    f.write("# 📟 Calculator Index\n\n")
    f.write("Click a link to open the notebook in the JupyterLite environment:\n\n")

    for ipynb in sorted(calc_root.rglob("*.ipynb")):
        if "__pycache__" in ipynb.parts or "shared" in ipynb.parts:
            continue

        name = ipynb.stem.replace("_", " ").title()
        rel_path = ipynb.relative_to(calc_root).as_posix()
        # <-- prepend 'calculators/'
        jlite_link = f"./{jupyterlite_base_url}calculators/{rel_path}"
        f.write(f"- [{name}]({jlite_link})\n")
