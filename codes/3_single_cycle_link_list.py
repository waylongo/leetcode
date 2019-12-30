class Node(object):
    """single cycle link list unit - node"""

    def __init__(self, item):
        self.item = item
        self.next = None


class SingleCycleLinkList(object):
    """single cycle link list"""

    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        if self.is_empty():
            return 0
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        if self.is_empty():
            return

        while cur.next != self.__head:
            print(cur.item, end=" ")
            cur = cur.next
        print(cur.item)

    def add(self, item):
        node = Node(item)

        if self.is_empty():
            self.__head = node
            node.next = self.__head
            return

        node.next = self.__head
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        cur.next = node
        self.__head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
            return
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        cur.next = node
        node.next = self.__head

    def insert(self, pos, item):
        if pos <=0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            pre = self.__head
            node = Node(item)
            while pos - 1:
                pre = pre.next
                pos -= 1
            if pre.next:
                node.next = pre.next
                pre.next = node
            else:
                pre.next = node

    def remove(self, item):
        if self.is_empty():
            return
        elif self.length() == 1:
            if self.__head.item == item:
                self.__head = None
        else:
            pre = self.__head
            if pre.item == item:
                # to remove the first element
                while pre.next != self.__head:
                    pre = pre.next
                pre.next = self.__head.next
                self.__head = self.__head.next
            else:
                # to remove middle element
                while pre.next != self.__head:
                    if pre.next.item == item:
                        pre.next = pre.next.next
                    pre = pre.next
    def search(self, item):
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.item == item:
                return True
            cur = cur.next
        return cur.item == item

if __name__ == "__main__":
    ll = SingleCycleLinkList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.travel()
    ll.append(4)
    ll.append(5)
    ll.travel()
    ll.insert(4, 6)
    ll.travel()
    ll.remove(3)
    ll.travel()
    print(ll.search(2))
    print(ll.search(5))
    print(ll.search(3))