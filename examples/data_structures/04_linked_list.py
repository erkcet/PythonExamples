"""Singly linked list implementation."""


class Node:
    """A single node in the linked list."""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    """Singly linked list with head pointer."""

    def __init__(self):
        self.head = None

    def prepend(self, data):
        """Insert a node at the beginning."""
        self.head = Node(data, self.head)

    def append(self, data):
        """Insert a node at the end."""
        if not self.head:
            self.head = Node(data)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(data)

    def to_list(self):
        """Convert to a Python list for display."""
        result, cur = [], self.head
        while cur:
            result.append(cur.data)
            cur = cur.next
        return result

    def __repr__(self):
        return " -> ".join(map(str, self.to_list()))


if __name__ == "__main__":
    ll = LinkedList()
    for v in [3, 5, 7]:
        ll.append(v)
    ll.prepend(1)
    print(f"List: {ll}")
