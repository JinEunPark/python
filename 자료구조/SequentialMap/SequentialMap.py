from Entry import Entry


class SquentialMap:
    def __init__(self):
        self.table = []

    def size(self):
        return len(self.table)

    def display(self):
        for i in range(len(self.table)):
            print(self.table[i], end=" || ")
        print()

    def insert(self, key, value):
        entry = Entry(key, value)
        self.table.append(entry)

    def search(self, key):
        for i in range(len(self.table)):
            if self.table[i].key == key:
                return self.table[i]
            else:
                return None

    def delete(self, key):
        for i in range(self.size()):
            if self.table[i].key == key:
                self.table.pop(i)
                return
# 마지막 줄에서 return을 실행하지 않으면 pop연산이 실행되고 나서도 반복문이 실행되는데 이렇게 반복문지 pop연산 이후에도 실행되면 index의 반복문의 인데스 번위는 줄지 않아서
# outif bound 오류가 발생한다.

sm = SquentialMap()
for i in range(10):
    sm.insert(i, i + i * 3)
sm.display()
for i in range(3):
    sm.delete(i)
sm.display()
