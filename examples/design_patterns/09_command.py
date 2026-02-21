"""Command pattern: encapsulate actions as objects with undo support."""


class TextEditor:
    """Simple text buffer that commands operate on."""
    def __init__(self):
        self.text = ""

    def __str__(self):
        return repr(self.text)


class InsertCommand:
    """Command to insert text at the end."""
    def __init__(self, editor: TextEditor, chars: str):
        self.editor = editor
        self.chars = chars

    def execute(self):
        self.editor.text += self.chars

    def undo(self):
        self.editor.text = self.editor.text[: -len(self.chars)]


class CommandInvoker:
    """Executes commands and maintains history for undo."""
    def __init__(self):
        self._history = []

    def run(self, command):
        command.execute()
        self._history.append(command)

    def undo(self):
        if self._history:
            self._history.pop().undo()


if __name__ == "__main__":
    editor = TextEditor()
    invoker = CommandInvoker()
    for word in ("Hello", " ", "World"):
        invoker.run(InsertCommand(editor, word))
        print(f"After insert: {editor}")
    invoker.undo()
    print(f"After undo:   {editor}")
