import random as random

from Entry import Entry


class binaryMap:
    def __init__(self):
        self.list = []

    def size(self):
        return len(self.list)

    def isEmpty(self):
        return len(self.list) == 0

    def insert(self, value, key):
        self.list.append(Entry(key, value))
        self.sort()

    def sort(self):
        for i in range(len(self.list)):
            key = self.list[i]
            j = i - 1
            while j > 0 and self.list[j].key > key.key:
                self.list[j + 1] = self.list[j]
                j -= 1
            self.list[j + 1] = key

    def search(self, key):

        low = 0
        high = len(self.list) - 1

        while high >= low:
            mid = (high + low) // 2
            if self.list[mid].key == key:
                return self.list[mid].value

            if self.list[mid].key < key:
                low = mid + 1
            else:
                high = mid - 1
        return None

    def display(self):
        for i in range(len(self.list)):
            print(self.list[i])


bm = binaryMap()

for i in range(8):
    bm.insert(int(random.random() * 10), int(random.random() * 10))

bm.display()

print(bm.search(5))
