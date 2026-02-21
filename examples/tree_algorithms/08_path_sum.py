"""Root-to-leaf path sum check in a binary tree."""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def has_path_sum(root, target):
    """Return True if any root-to-leaf path sums to target."""
    if root is None:
        return False
    target -= root.val
    if root.left is None and root.right is None:
        return target == 0
    return has_path_sum(root.left, target) or has_path_sum(root.right, target)


def all_path_sums(root, current=0):
    """Return a list of all root-to-leaf path sums."""
    if root is None:
        return []
    current += root.val
    if root.left is None and root.right is None:
        return [current]
    return all_path_sums(root.left, current) + all_path_sums(root.right, current)


if __name__ == "__main__":
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    tree = Node(5, Node(4, Node(11)), Node(8, Node(13), Node(4)))
    print(f"All root-to-leaf sums: {all_path_sums(tree)}")
    print(f"Has path sum 20: {has_path_sum(tree, 20)}")
    print(f"Has path sum 26: {has_path_sum(tree, 26)}")
