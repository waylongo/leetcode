class Node(object):
    def __init__(self, elem, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        """add element in the tree"""
        node = Node(elem)

        if self.root is None:
            self.root = node
        else:
            queue = [self.root]
            while queue:
                cur = queue.pop(0)
                if cur.lchild is None:
                    cur.lchild = node
                    return
                elif cur.rchild is None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def preorder(self, root):

        if root is None:
            return
        print(root.elem, end=" ")
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self, root):

        if root is None:
            return
        self.inorder(root.lchild)
        print(root.elem, end=" ")
        self.inorder(root.rchild)

    def postorder(self, root):

        if root is None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem, end=" ")

    def breath_travel(self, root):
        if root is None:
            return

        queue = [root]
        while queue:
            cur = queue.pop(0)
            print(cur.elem, end=" ")
            if cur.lchild:
                queue.append(cur.lchild)
            if cur.rchild:
                queue.append(cur.rchild)


if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.preorder(tree.root)
    print("")
    tree.inorder(tree.root)
    print("")
    tree.postorder(tree.root)
    print("")
    tree.breath_travel(tree.root)
