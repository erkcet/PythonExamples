"""Abstract Factory pattern: create families of related objects."""

from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self) -> str: ...

class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str: ...

class WinButton(Button):
    def render(self): return "[Windows Button]"

class WinCheckbox(Checkbox):
    def render(self): return "[Windows Checkbox]"

class MacButton(Button):
    def render(self): return "(Mac Button)"

class MacCheckbox(Checkbox):
    def render(self): return "(Mac Checkbox)"


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: ...
    @abstractmethod
    def create_checkbox(self) -> Checkbox: ...

class WindowsFactory(GUIFactory):
    def create_button(self): return WinButton()
    def create_checkbox(self): return WinCheckbox()

class MacFactory(GUIFactory):
    def create_button(self): return MacButton()
    def create_checkbox(self): return MacCheckbox()


def build_ui(factory: GUIFactory):
    """Build a UI using the given factory."""
    print(factory.create_button().render())
    print(factory.create_checkbox().render())


if __name__ == "__main__":
    for factory in (WindowsFactory(), MacFactory()):
        build_ui(factory)
        print()
