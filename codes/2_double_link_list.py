
class Node(object):
    """double link list unit - node"""
    def __init__(self, item):
        """constructor"""
        self.item = item
        self.next = None
        self.prev = None

class DLinkList(object):
    """double link list"""
    def __init__(self):
        """constructor"""
        self.__head = None

    def is_empty(self):
        """check if list is empty"""
        return self.__head == None

    def length(self):
        """return the length of the list"""
        cur = self.__head
        count = 0
        while cur:
            cur = cur.next
            count += 1

        return count

    def travel(self):
        """print all elements in the list"""
        cur = self.__head

        while cur:
            print(cur.item, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """add item in the front"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            return
        node.next = self.__head
        self.__head.prev = node
        self.__head = node

    def append(self, item):
        """append item in the tail"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            return
        cur = self.__head
        while cur.next:
            cur = cur.next
        cur.next = node
        node.prev = cur

    def search(self, item):
        """check if item exists in the list"""
        cur = self.__head
        while cur:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def insert(self, pos, item):
        """insert item on pos index"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            pre = self.__head
            while pos - 1:
                pre = pre.next
                pos -= 1
            node.next = pre.next
            pre.next = node
            node.next.prev = node
            node.prev = pre

    def remove(self, item):
        """remove item in the list"""
        # list is empty
        if self.is_empty():
            return
        # remove the first element
        pre = self.__head
        if pre.item == item:
            if pre.next:
                self.__head = pre.next
                pre.next.prev = None
                return
            else:
                self.__head = None

        # middle
        while pre.next:
            if pre.next.item == item:
                if pre.next.next:
                    pre.next = pre.next.next
                    pre.next.prev = pre #?
                else:
                    pre.next = None
                return
            pre = pre.next

if __name__ == "__main__":
    """testing"""

    dll = DLinkList()
    dll.add(1)
    dll.add(2)
    dll.add(3)
    dll.add(4)
    dll.travel()
    dll.insert(3, 9)
    dll.travel()
    dll.remove(2)
    dll.travel()