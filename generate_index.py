import os

def make_index(folder):
    entries = sorted(os.listdir(folder))
    entries = [e for e in entries if e != "index.html"]
    lines = ['<html><body>']
    for e in entries:
        full = os.path.join(folder, e)
        name = e + ("/" if os.path.isdir(full) else "")
        lines.append(f'<a href="{name}">{name}</a><br>')
    lines.append('</body></html>')
    with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    for e in entries:
        full = os.path.join(folder, e)
        if os.path.isdir(full):
            make_index(full)

make_index(os.path.join("docs", "zips"))
print("Index files created.")