class Stack:
    def __init__(self):
        self.head = None

    def push(self, val):
        if self.head is None:
            self.head = Node(val)
            return
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None: return -1
        val = self.head.val
        self.head = self.head.next
        return val

    def peek(self):
        return self.head.val if self.head is None else -1

    def is_empty(self):
        return self.head is None


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 4):
        print("Adding:", i)
        stack.push(i)

    print("Top of the Stack:", stack.peek())
    print("Is Stack Empty:", stack.is_empty())

    for i in range(1, 4):
        print("Removing:", stack.pop())