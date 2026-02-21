"""Mirror / invert a binary tree."""

from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def invert(root):
    """Invert the tree in-place and return the root."""
    if root is None:
        return None
    root.left, root.right = invert(root.right), invert(root.left)
    return root


def level_order(root):
    """Return level-order list for display."""
    if not root:
        return []
    result, q = [], deque([root])
    while q:
        node = q.popleft()
        result.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return result


if __name__ == "__main__":
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    print(f"Before invert: {level_order(tree)}")
    invert(tree)
    print(f"After invert:  {level_order(tree)}")
