class Node(object):
    """single cycle link list unit - node"""
    def __init__(self, item):
        self.item = item
        self.next = None

class SingleCycleLinkList(object):
    """single cycle link list"""
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def length(self):
        cur = self.head
        if self.is_empty():
            return 0
        count = 1
        while cur.next !=self.head
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.head
        if self.is_empty():
            return

        while cur.next !=self.head:
            print(cur.item)
            cur = cur.next
        print(cur)