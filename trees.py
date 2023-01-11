import random

class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def addNode(self, val):
        if val == self.val:
            raise ValueError("Duplicate value!")
        elif val < self.val:
            if self.left:
                self.left.addNode(val)
            else:
                self.left = BSTNode(val)
        else:
            if self.right:
                self.right.addNode(val)
            else:
                self.right = BSTNode(val)

    def traverse(self, prefix = ""):
        print(prefix + str(self.val))
        if self.left:
            self.left.traverse(prefix=prefix + "<-")
        if self.right:
            self.right.traverse(prefix=prefix + "->")


    def search(self, val):
        if val == self.val:
            return True
        else:
            if val < self.val:
                if self.left:
                    return self.left.search(val)
            else:
                if self.right:
                    return self.right.search(val)
        return False

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def addNode(self, value):
        if self.left is None:
            self.left = BinaryTreeNode(value)
        elif self.right is None:
            self.right = BinaryTreeNode(value)
        else:
            if bool(random.getrandbits(1)):
                self.left.addNode(value)
            else:
                self.right.addNode(value)

    def __str__(self):
        buffer = []
        if self:
            buffer.append(str(self.left))
            buffer.append(str(self.value))
            buffer.append(str(self.right))
        return ",".join(buffer)

root = BSTNode(0)
root.addNode(4)
root.addNode(7)
root.addNode(1)
root.addNode(8)
root.traverse()

print(root.search(18))
print(root.search(8))
print(root.search(11))