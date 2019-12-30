class Stack(object):
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def size(self):
        return len(self.item)

    def push(self, item):
        return self.item.append(item)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[len(self.item) - 1]


if __name__ == "__main__":
    stack = Stack()
    stack.push("hello")
    stack.push("world")
    stack.push("itcast")
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())