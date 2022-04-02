from Set import Set as Set

list = []

for i in range(5):
    list.insert(i, (i + 1) * 10)

print(list)

list.insert(1, 60)


# 파이선의 리스트는 동적할당 되어 있어서 기존에 주어진 메모리보다 더 큰 data가 들어오는 경우에는 다시 리스트를 생성하는 과정을 거치기 대문에 대부분의 경우 o(1)으로 표현한것이다


def find_max(list):
    max = list[0]
    min = list[0]
    for i in list:
        if i > max:
            max = i
        if i < min:
            min = i
    return (max, min)


def compare(lista, listb):
    for i in lista:
        for e in listb:
            if i == e:
                return True
    return False


def combinList(lista, listb):
    lista.extend(listb)
    return lista.sort()


class upgradSet(Set):
    
    def __init__(self):
        super(upgradSet, self).__init__()

    def findProperSubset(self, seta): #  진 부분 집합을 가려내는 매소드
        if self.Set == super(upgradSet, self).inetersect(seta):
            return True
        else:
            return False


setc = upgradSet()
setf = upgradSet()
for i in range(10):
    setc.insert(i)

for e in range(5, 16):
    setf.insert(i)
print(setc.findProperSubset(setf))
