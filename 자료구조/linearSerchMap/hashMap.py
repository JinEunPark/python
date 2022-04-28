from Entry import Entry
import random

class hashMap:
    def __init__(self, max):
        self.max = max
        self.list = [None] * self.max

    def isEmpty(self):
        return len(self.list) == 0

    def hashFn(self, key):
        hashAdress = key % self.max
        return hashAdress

    def insert(self, key, value):

        entry = Entry(key, value)
        index = self.hashFn(key)

        if self.list[index] is not None:
            i = 0
            while self.list[index + i] == None:
                i += 1
                if index + i > self.max:
                    index = 0
                    i = 0
            self.list[index + i] = entry
        else:
            self.list[index] = entry

    def delete(self, key):

        index = self.hashFn(key)

        if self.list[index].key == key:
            value = self.list[index].value
            self.list.append(index)
            return value
        else:
            i = 0
            while self.list[index + i].key == key:
                i += 1

            value = self.list[index].value
            self.list.append(index)
            return value


    def display(self):
        for i in range(self.max):
            print(self.list[i])
hash = hashMap(10)

for i in range(10):
    hash.insert(1,int(random.random()*10))

hash.display()


