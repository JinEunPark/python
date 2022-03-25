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
            self.list.sort(reverse=True)
        elif bool == False:
            self.list.sort(reverse=False)

    def merge(self, listA):
        self.list.extend(listA)

    def append(self, item):
        self.list.append(item)

    def __str__(self):
        return str(self.list)


Arraylist = Arraylist()
for i in range(100):
    Arraylist.append(i+1)

print(Arraylist)
