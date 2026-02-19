from pathlib import Path

Path("sample.txt").write_text("line1\nline2\n", encoding="utf-8")
text = Path("sample.txt").read_text(encoding="utf-8")
print(text.strip())
