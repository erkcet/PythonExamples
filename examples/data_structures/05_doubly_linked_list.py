"""Doubly linked list implementation."""


class Node:
    """Node with prev and next pointers."""

    def __init__(self, data, prev=None, nxt=None):
        self.data, self.prev, self.next = data, prev, nxt


class DoublyLinkedList:
    """Doubly linked list with head and tail pointers."""

    def __init__(self):
        self.head = self.tail = None

    def append(self, data):
        """Add a node at the end."""
        node = Node(data, prev=self.tail)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def pop(self):
        """Remove and return the last element."""
        if not self.tail:
            raise IndexError("pop from empty list")
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return data

    def forward(self):
        """Return elements front to back."""
        cur, result = self.head, []
        while cur:
            result.append(cur.data)
            cur = cur.next
        return result

    def backward(self):
        """Return elements back to front."""
        cur, result = self.tail, []
        while cur:
            result.append(cur.data)
            cur = cur.prev
        return result


if __name__ == "__main__":
    dll = DoublyLinkedList()
    for v in [1, 2, 3, 4]:
        dll.append(v)
    print(f"Forward:  {dll.forward()}")
    print(f"Backward: {dll.backward()}")
    print(f"Popped:   {dll.pop()}")
