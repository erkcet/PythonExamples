from tempfile import NamedTemporaryFile

with NamedTemporaryFile("w+", encoding="utf-8", delete=True) as f:
    f.write("temporary data")
    f.seek(0)
    print(f.read())
