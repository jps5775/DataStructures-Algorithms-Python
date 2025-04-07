class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def add(self, val):
        if self.back is None:
            self.back = Node(val)
            self.front = self.back
            return
        new_node = Node(val)
        self.back.next = new_node
        self.back = new_node

    def remove(self):
        if self.front is None:
            return -1
        val = self.front.val
        self.front = self.front.next
        if self.front is None:
            self.back = None
        return val

    def is_empty(self):
        return self.front is None

    def peek(self):
        return self.front.val if self.front is not None else -1

    def __str__(self):
        curr = self.front
        vals = []
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return str(vals)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

if __name__ == "__main__":
    q = Queue()
    for i in range(3):
        q.add(i)

    print(q)
    q.remove()
    print(q)
    q.remove()
    print(q)
    q.remove()
    print(q)
    q.remove()
    print(q)