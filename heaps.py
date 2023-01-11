class MinHeap:

    # empty heap
    def __init__(self):
        self.items = []

    # O(log N) for N items
    def insert(self, item):
        self.items.append(item)
        size = len(self.items)
        index = size - 1
        parent = (index - 1) // 2

        while parent >= 0:
            if self.items[parent] > self.items[index]:
                self.items[parent], self.items[index] = self.items[index], self.items[parent]
                index = parent
                parent = (index - 1) // 2
            else:
                break


    # O(log N) for N items
    def deletemin(self):
        replaced = self.items.pop()
        minvalue = self.items[0]
        self.items[0] = replaced

        length = len(self.items)
        index = 0
        while True:
            left = 2*index + 1
            right = 2*index + 2

            if left >= length:
                # no left no right
                break
            elif ((left < length) and (right >= length)):
                # just left
                if self.items[index] > self.items[left]:
                    self.items[index], self.items[left] = self.items[left], self.items[index]
                    break
            else:
                # both left and right

                # the heap property is already satisfied?
                if ((self.items[index] < self.items[left]) and
                    (self.items[index] < self.items[right])):
                    break

                if self.items[right] > self.items[left]:
                    self.items[index], self.items[left] = self.items[left], self.items[index]
                    index = left
                else:
                    self.items[index], self.items[right] = self.items[right], self.items[index]
                    index = right

        return minvalue

    # O(N log N) for N items
    def heapify(self, items):
        for item in items:
            self.insert(item)

heap = MinHeap()

heap.heapify([3, 10, 5, 11, 12, 6, 8, 15, 20, 13])

heap.insert(7)

for i in range(4):
    print('\nheap contents:', heap.items)
    print(heap.deletemin(), 'deleted')
    print('heap contents:', heap.items)
