class Queue(object):
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def size(self):
        return len(self.item)

    def enqueue(self, item):
        return self.item.append(item)

    def dequeue(self):
        return self.item.pop(0)


if __name__ == "__main__":
    q = Queue()
    q.enqueue("hello")
    q.enqueue("world")
    q.enqueue("itcast")
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
