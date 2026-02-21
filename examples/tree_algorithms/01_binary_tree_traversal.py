"""Binary tree traversals: inorder, preorder, postorder."""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def inorder(root):
    """Return nodes in left-root-right order."""
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def preorder(root):
    """Return nodes in root-left-right order."""
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def postorder(root):
    """Return nodes in left-right-root order."""
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


if __name__ == "__main__":
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3))
    print(f"Inorder:   {inorder(tree)}")
    print(f"Preorder:  {preorder(tree)}")
    print(f"Postorder: {postorder(tree)}")
