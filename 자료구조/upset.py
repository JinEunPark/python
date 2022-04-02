from Set import Set


class newSet(Set):
    def __init__(self):
        super(newSet, self).__init__()

    def contains(self, item):
        for i in self.Set:
            if item == i:
                return True
        return False

    def delete(self, item):
        if self.contains(item):
            self.Set.pop(item)

    def insert(self, item):
        if self.contains(item):
            Set.insert(item)

    def intersect(self, Setb):
        rSet = newSet()
        for i in Setb:
            if self.contains(i):
                rSet.insert(i)
        return rSet

    def union(self, Setb):
        rSet = self.Set
        for i in Setb:
            if self.contains(i):
                continue
            else:
                rSet.append(i)
        return rSet

    def diffence(self, Setb):
        rSet = newSet()
        for i in Setb:
            if self.Set.__contains__(i):
                continue
            else:
                rSet.insert(i)
        return rSet

    def isSubsetOf(self, otherSet):
        for i in self.Set:
            if otherSet.contains(i):
                continue
            else:
                return False
        return True

    def __str__(self):
        return str(self.Set)


set = newSet()
for i in range(10):
    set.insert(i)
set.delete(9)
print(set)
