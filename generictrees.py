class Node:

    def __init__(self, value):
        self.value = value
        self.children = []


    def addChild(self, child):
        #if len(self.children) < 2:

        self.children.append(child)

        #else:
        #    raise ValueError("Sorry, this is a binary tree")


root = Node(0)

node1 = Node(2)

root.addChild(node1)

node2 = Node(111)

node1.addChild(node2)