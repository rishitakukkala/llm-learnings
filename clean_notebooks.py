import nbformat, glob

for path in glob.glob("notebooks/*.ipynb"):
    nb = nbformat.read(path, as_version=4)
    if "widgets" in nb.get("metadata", {}):
        del nb["metadata"]["widgets"]
        nbformat.write(nb, open(path, "w", encoding="utf-8"))
        print(f"🧹 Cleaned {path}")
    else:
        print(f"✅ No widget metadata in {path}")
