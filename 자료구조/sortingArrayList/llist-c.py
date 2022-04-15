import random as random
class Arraylist:
    def __init__(self):
        self.list = []

    def insert(self, pos, item):
        self.list[pos] = item

    def delelte(self, pos):
        return self.list.append(pos)

    def isEmpty(self):
        if len(self.list) == 0:
            return True

    def getEntry(self, pos):
        return self.list[pos]

    def size(self):
        return len(self.list)

    def clear(self):
        self.list.clear(self)

    def find(self, item):
        return self.list.index(item)

    def replace(self, pos, item):
        self.replace(pos, item)

    def sort(self, bool):
        if bool == True:
            for i in range(len(self.list)):
                least = i
                for e in range(i + 1, len(self.list)):
                    if self.list[least] > self.list[e]:
                        least = e
                self.list[least], self.list[i] = self.list[i], self.list[least]
            return
        else:
            for i in range(len(self.list)):
                most = i
                for e in range(i + 1, len(self.list)):
                    if self.list[most] < self.list[e]:
                        most = e
                    self.list[most], self.list[i] = self.list[i], self.list[most]

    def merge(self, listA):
        self.list.extend(listA)

    def append(self, item):
        self.list.append(item)

    def __str__(self):
        return str(self.list)


Arraylist = Arraylist()
for i in range(10):
    Arraylist.append(int(random.random()*10))

print(Arraylist)

Arraylist.sort(False)

print(Arraylist)
