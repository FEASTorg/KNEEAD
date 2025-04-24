from pathlib import Path

calc_root = Path("calculators")
output_md = Path("docs/calculators_index.md")
jupyterlite_base_url = "lite/lab/index.html?path=calculators"

with output_md.open("w", encoding="utf-8") as f:
    f.write("# 📟 Calculators Index\n\n")
    f.write("Click to open each notebook in the JupyterLite environment:\n\n")

    for ipynb in sorted(calc_root.rglob("*.ipynb")):
        if "__pycache__" in ipynb.parts or "shared" in ipynb.parts:
            continue

        name = ipynb.stem.replace("_", " ").title()
        rel_path = ipynb.relative_to(calc_root).as_posix()  # ✅ fixes the slashes
        jlite_link = f"./{jupyterlite_base_url}/{rel_path}"
        f.write(f"- [{name}]({jlite_link})\n")
