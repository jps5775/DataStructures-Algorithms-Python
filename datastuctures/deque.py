class Deque:
    def __init__(self):
        self.front = Node(-1)
        self.back = Node(-1)
        self.front.next = self.back
        self.back.prev = self.front

    def add_front(self, val):
        new_node = Node(val)
        next = self.front.next
        self.front.next = new_node
        new_node.next = next
        next.prev = new_node
        new_node.prev = self.front

    def remove_front(self):
        if self.front.next == self.back:
            return
        next = self.front.next.next
        self.front.next = next
        next.prev = self.front

    def add_back(self, val):
        prev = self.back.prev
        new_node = Node(val)
        self.back.prev = new_node
        new_node.prev = prev
        prev.next = new_node
        new_node.next = self.back

    def remove_back(self):
        if self.back.prev == self.front:
            return
        prev = self.back.prev.prev
        prev.next = self.back
        self.back.prev = prev

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

if __name__ == "__main__":
    d = Deque