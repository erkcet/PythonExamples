"""Serialize and deserialize a binary tree to/from a string."""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def serialize(root):
    """Encode a tree into a comma-separated string (preorder with nulls)."""
    if root is None:
        return "#"
    return f"{root.val},{serialize(root.left)},{serialize(root.right)}"


def deserialize(data):
    """Decode a string back into a binary tree."""
    tokens = iter(data.split(","))

    def _build():
        val = next(tokens)
        if val == "#":
            return None
        node = Node(int(val))
        node.left = _build()
        node.right = _build()
        return node

    return _build()


def inorder(root):
    """Helper to display tree contents."""
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


if __name__ == "__main__":
    tree = Node(1, Node(2, Node(4), None), Node(3, None, Node(5)))
    s = serialize(tree)
    print(f"Serialized:   {s}")
    restored = deserialize(s)
    print(f"Deserialized: {inorder(restored)}")
