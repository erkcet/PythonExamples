"""Lowest Common Ancestor (LCA) in a binary tree."""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def lca(root, p, q):
    """Return the lowest common ancestor node of nodes with values p and q.

    Assumes both p and q exist in the tree.
    """
    if root is None or root.val == p or root.val == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root
    return left if left else right


if __name__ == "__main__":
    #       3
    #      / \
    #     5   1
    #    / \
    #   6   2
    tree = Node(3, Node(5, Node(6), Node(2)), Node(1))
    result = lca(tree, 6, 2)
    print(f"LCA of 6 and 2: {result.val}")
    result = lca(tree, 6, 1)
    print(f"LCA of 6 and 1: {result.val}")
