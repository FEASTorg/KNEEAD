from pathlib import Path

# Paths
pages_dir = Path("docs/pages")
output_md = Path("docs/pages_index.md")

# Start writing index
with output_md.open("w", encoding="utf-8") as f:
    f.write("# 📚 Design Document Index\n\n")

    for md in sorted(pages_dir.glob("*.md")):
        if md.name == "index.md":
            continue
        name = md.stem.replace("_", " ").title()
        rel_link = f"./pages/{md.name}"
        f.write(f"- [{name}]({rel_link})\n")
