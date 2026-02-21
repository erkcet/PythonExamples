"""Binary search tree implementation."""


class Node:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None


def insert(root, key):
    """Insert a key and return the (possibly new) root."""
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root


def search(root, key):
    """Return True if key exists in the BST."""
    if root is None:
        return False
    if key == root.key:
        return True
    return search(root.left, key) if key < root.key else search(root.right, key)


def inorder(root):
    """Return keys in sorted (inorder) sequence."""
    if root is None:
        return []
    return inorder(root.left) + [root.key] + inorder(root.right)


if __name__ == "__main__":
    root = None
    for k in [5, 3, 7, 1, 4, 6, 8]:
        root = insert(root, k)
    print(f"Inorder: {inorder(root)}")
    print(f"Search 4: {search(root, 4)}")
    print(f"Search 9: {search(root, 9)}")
