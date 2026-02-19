class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __repr__(self):
        return f"Book(title={self.title!r}, pages={self.pages!r})"

book = Book("Python 101", 200)
print(str(book))
print(repr(book))
