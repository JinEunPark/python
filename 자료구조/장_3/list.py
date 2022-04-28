class list:
    def __init__(self):
        self.list = []

    def insert(self, pos, item):

        self.list.insert(pos, item)

    def delete(self, pos):
        data = self.list[pos]
        self.list.delete(pos)
        return data

    def isEmpty(self):
        return self.len(list) == 0

    def getEntry(self, pos):
        return self.list[pos]

    def size(self):
        return len(self.list)

    def clear(self):
        self.list = []

    def sort(self, bol):
        if bol:
            self.list.sort()  # sort : 정렬, 기본값은 오름차순 정렬, reverse옵션 True는 내림차순 정렬

        else:
            self.list.sort(reverse=True)

    def find(self, item):
        return self.list.index(item)  # list에 존재하는 item값을 반환하는 함수

    def replace(self, item, pos):
        self.list[pos] = item

    def merge(self, lst):
        self.list.extend(lst)

    def display(self, msg="arraylist"):
        print(msg, self.size(), self.list)

    def append(self, item):
        self.list.append(item)
