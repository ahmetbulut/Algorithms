class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        #if empty list
        if not self.head:
            self.head = Node(data)
            return

        # if not empty, find the node at the end of the list
        current = self.head
        while current.next:
            current = current.next

        #insert there at the end
        current.next = Node(data)

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            else:
                current = current.next
        return False

    def remove(self, target):
        current = self.head
        if current:
            if current.data == target:
                self.head = current.next
                return
            else:
                # while there are succeeding nodes
                while current.next:
                    if current.next.data == target:
                        current.next = current.next.next
                        return
                    else:
                        current = current.next
        # if reached here, target not found!

    def __str__(self):
        items = []
        current = self.head
        while current:
            items.append(current.data)
            current = current.next
        return ",".join(items)

a_list = LinkedList()
a_list.append("Tuesday")
a_list.append("Wednesday")
a_list.append("Friday")
a_list.remove("Wednesday")
print(a_list)

#a_list.remove("uesday")

#a_list.append("Friday")

#print(a_list)
