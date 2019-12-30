class Deque(object):
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def size(self):
        return len(self.item)

    def add_front(self, item):
        return self.item.insert(0, item)

    def add_rear(self, item):
        return self.item.append(item)

    def remove_front(self):
        return self.item.pop(0)

    def remove_rear(self):
        return self.item.pop()


if __name__ == "__main__":
    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print(deque.size())
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque.remove_rear())
    print(deque.remove_rear())
