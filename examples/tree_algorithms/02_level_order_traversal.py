"""Level-order (BFS) traversal of a binary tree."""

from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def level_order(root):
    """Return a list of lists, each being one level of the tree."""
    if root is None:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


if __name__ == "__main__":
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(6)))
    for i, level in enumerate(level_order(tree)):
        print(f"Level {i}: {level}")
