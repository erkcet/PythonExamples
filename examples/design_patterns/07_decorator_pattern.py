"""Decorator pattern (GoF): wrap objects to add behavior dynamically."""

from abc import ABC, abstractmethod


class TextComponent(ABC):
    """Abstract text component."""
    @abstractmethod
    def render(self) -> str: ...


class PlainText(TextComponent):
    """Concrete component returning raw text."""
    def __init__(self, text: str):
        self._text = text

    def render(self) -> str:
        return self._text


class BoldDecorator(TextComponent):
    """Wraps text in bold markers."""
    def __init__(self, wrapped: TextComponent):
        self._wrapped = wrapped

    def render(self) -> str:
        return f"**{self._wrapped.render()}**"


class ItalicDecorator(TextComponent):
    """Wraps text in italic markers."""
    def __init__(self, wrapped: TextComponent):
        self._wrapped = wrapped

    def render(self) -> str:
        return f"_{self._wrapped.render()}_"


def demonstrate_decorator_pattern():
    """Show stacking decorators on a component."""
    plain = PlainText("Hello")
    bold = BoldDecorator(plain)
    bold_italic = ItalicDecorator(bold)
    print(f"Plain:       {plain.render()}")
    print(f"Bold:        {bold.render()}")
    print(f"Bold+Italic: {bold_italic.render()}")


if __name__ == "__main__":
    demonstrate_decorator_pattern()
