"""Check if a binary tree is height-balanced."""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def is_balanced(root):
    """Return True if the tree is balanced (heights differ by at most 1).

    Uses a bottom-up approach returning -1 to signal imbalance early.
    """
    def _check(node):
        if node is None:
            return 0
        left = _check(node.left)
        if left == -1:
            return -1
        right = _check(node.right)
        if right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return _check(root) != -1


if __name__ == "__main__":
    balanced = Node(1, Node(2, Node(4), Node(5)), Node(3))
    unbalanced = Node(1, Node(2, Node(3, Node(4), None), None), None)
    print(f"Balanced tree:   {is_balanced(balanced)}")
    print(f"Unbalanced tree: {is_balanced(unbalanced)}")
