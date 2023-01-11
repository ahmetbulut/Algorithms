class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if self.head is None:
            raise IndexError('pop from empty stack')

        poppednode = self.head
        self.head = self.head.next

        return poppednode.data

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        node = Node(item)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            raise IndexError('pop from empty queue')

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return temp.data


q = Queue()
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())