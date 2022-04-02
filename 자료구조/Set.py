class Set:
    def __init__(self):
        self.Set = []

    def size(self):
        return len(self.Set)

    def contains(self, item):
        return item in self.Set

    def insert(self, item):
        if item not in self.Set:
            self.Set.append(item)  # set을 구현하는 거니까 indexnumber 생략

    def delete(self, item):
        index = self.Set.index(item)  # value 가 들어있는 리스트의 index를 얻어서 index에 저장
        self.Set.pop(index)  # 반환하고 삭제

    def equals(self, setB):
        self.Set.sort()
        setB.sort()
        for i in self.Set:
            for e in setB:
                if i != e:
                    return False
        return True

    def union(self, setB):
        for i in setB.Set:
            if i in self.Set:
                continue
            else:
                self.Set.append(i)

    def inetersect(self, setB):

        interSet = []
        for i in setB.Set:
            if i in setB:
                interSet.append(i)
        return interSet

    def diffence(self, setB):

        differ = []

        for i in setB:
            if i in self.Set:
                continue
            else:
                differ.append(i)
        return differ

    def display(self):
        print(str(self.Set))

    def __contains__(self, item):
        if item in self.Set:
            return True
        else: return False

    def __iter__(self):
        return iter(self.Set)



