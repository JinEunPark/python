class array_2:
    def __init__(self):
        self.list = []

    def insert(self, pos, item):
        list2 = [i for i in range(pos, len(self.list))]

        # 넘어온 인덱스 밖의 리스트 요소를 새로운 리스트에 담는다
        for i in range(pos, len(self.list)):
            self.list.pop(pos)  # 주어진 인덱스 뒤로 코드 값 삭제함 여기서 문제가 파이썬은 하나를 날리고 나면 리스트 자체가 줄든다는거다.
        self.list.append(item)
        self.list.extend(list2)

    def delete(self, pos):
        list2 = [x for x in range(pos, len(self.list))]
        for i in range(pos, len(self.list)):
            self.list.pop(-1)
        self.list.extend(list2)

    def extend(self, listb):
        length = len(listb)
        s_length = len(self.list)
        for i in range(s_length, length+s_length):
            self.list.append(listb[i-s_length])


array = array_2()
for i in range(10):
    array.list.append(i)
print("insert 전:", array.list)
array.insert(2, 1000)
print("after insert", array.list)
array.delete(3)
print("after delete list", array.list)
listb =[ i for i in range(10)]
print(listb)
array.extend(listb)
print("after insert list",array.list)
