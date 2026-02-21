"""Trie (prefix tree) implementation."""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    """Prefix tree for efficient string storage and lookup."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the trie."""
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    def search(self, word):
        """Return True if the exact word is in the trie."""
        node = self._find(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        """Return True if any word starts with the given prefix."""
        return self._find(prefix) is not None

    def _find(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


if __name__ == "__main__":
    t = Trie()
    for word in ["apple", "app", "apply", "bat"]:
        t.insert(word)
    print(f"search 'app':    {t.search('app')}")
    print(f"search 'apt':    {t.search('apt')}")
    print(f"prefix 'app':    {t.starts_with('app')}")
