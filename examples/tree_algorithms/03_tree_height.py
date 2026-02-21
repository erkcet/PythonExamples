"""Calculate the height of a binary tree."""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def height(root):
    """Return the height of the tree (edges on longest root-to-leaf path).

    An empty tree has height -1; a single node has height 0.
    """
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))


def count_nodes(root):
    """Return the total number of nodes."""
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


if __name__ == "__main__":
    tree = Node(1, Node(2, Node(4), Node(5, Node(7), None)), Node(3))
    print(f"Height: {height(tree)}")
    print(f"Nodes:  {count_nodes(tree)}")
