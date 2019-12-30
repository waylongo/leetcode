class SingleNode(object):
    """single link list unit - node"""

    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    """single link list"""

    def __init__(self):
        """constructor"""
        self.__head = None

    def is_empty(self):
        """return boolean if the list is empty"""
        return self.__head == None

    def length(self):
        """return the length of list"""
        cur = self.__head
        count = 0

        while cur:
            count += 1
            cur = cur.next

        return count

    def travel(self):
        """print all elements in the list"""
        cur = self.__head

        while cur:
            print(cur.item, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """add element in the front"""
        node = SingleNode(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """append element in the tail"""
        node = SingleNode(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            return
        while cur.next:
            cur = cur.next
        cur.next = node

    def insert(self, pos, item):
        """insert item on pos index"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = SingleNode(item)
            pre = self.__head
            while pos - 1:
                pre = pre.next
                pos -= 1
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """remove item in the list"""
        pre = self.__head
        if pre.item == item:
            self.__head = pre.next
            return

        while pre.next:
            if pre.next.item == item:
                pre.next = pre.next.next
                return
            pre = pre.next

    def search(self, item):
        """check if item exists in the list"""
        cur = self.__head
        while cur:
            if cur.item == item:
                return True
            cur = cur.next
        return False


if __name__ == "__main__":
    """testing"""

    ll = SingleLinkList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.travel()
    ll.append(4)
    ll.travel()
    ll.insert(2, 9)
    ll.travel()
    ll.remove(5)
    ll.travel()
    print(ll.search(3))
    print(ll.search(10))
