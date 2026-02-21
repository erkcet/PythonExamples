"""Template Method pattern: define algorithm skeleton, defer steps."""

from abc import ABC, abstractmethod


class DataExporter(ABC):
    """Base class defining the export algorithm template."""

    def export(self, data):
        """Template method: fixed sequence of steps."""
        formatted = self.format_header()
        for item in data:
            formatted += self.format_row(item)
        formatted += self.format_footer()
        print(formatted)

    @abstractmethod
    def format_header(self) -> str: ...
    @abstractmethod
    def format_row(self, item) -> str: ...
    def format_footer(self) -> str:
        return ""


class CSVExporter(DataExporter):
    def format_header(self): return "name,score\n"
    def format_row(self, item): return f"{item[0]},{item[1]}\n"


class MarkdownExporter(DataExporter):
    def format_header(self): return "| Name | Score |\n|------|-------|\n"
    def format_row(self, item): return f"| {item[0]} | {item[1]} |\n"


if __name__ == "__main__":
    records = [("Alice", 95), ("Bob", 82), ("Carol", 91)]
    print("=== CSV ===")
    CSVExporter().export(records)
    print("=== Markdown ===")
    MarkdownExporter().export(records)
