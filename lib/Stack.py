class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            print("Stack is full")

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.items.pop()

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        try:
            index = self.items[::-1].index(target)
            return index  # Return the index from the top of the stack
        except ValueError:
            return -1