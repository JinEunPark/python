import random


class Maxheap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)

    def size(self):
        return len(self.heap) - 1

    def isEmpty(self):
        return self.size() == 0

    def display(self, string="maxheap"):
        print(string, self.heap[1:])

    def parent(self, index):
        return self.heap[index // 2]

    def Left(self, index):
        return self.heap[index * 2]

    def right(self, index):
        return self.heap[index * 2 + 1]

    def insert(self, data):

        self.heap.append(data)
        index = self.size()
        while index != 1 and data > self.parent(index):
            self.heap[index] = self.parent(index)
            index = index // 2

        self.heap[index] = data

    def delete(self):
        if not self.isEmpty():
            parent = 1
            child = 2
            last = self.heap[self.size()]
            hroot = self.heap[1]

            while child < self.size():

                if self.Left(parent) < self.right(parent):
                    child += 1
                if last > self.heap[child]:
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child = child * 2
        self.heap[parent] = last
        self.heap.pop(-1)
        return hroot


mh = Maxheap()
for i in range(10):
    mh.insert(random.randrange(0, 10))
mh.display()
print("delete:", end=" ")
for i in range(3):
    print(mh.delete(), end=" ")
mh.display()

