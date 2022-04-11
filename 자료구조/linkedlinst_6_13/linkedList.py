from node import node as Node


class linkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        count = 0
        node = self.head
        while node != None:
            node = node.link
            count += 1
        return count

    def getNode(self, pos):

        if pos < 0:
            return None

        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node

    def insert(self, pos, item):
        node = Node(item, None)
        if self.isEmpty():
            self.head = node
        else:
            before = self.getNode(pos - 1)
            node.link = before.link
            before.link = node

    def delete(self, pos):
        before = self.getNode(pos - 1)
        if before == None:
            if not self.isEmpty():
                data = self.head.data
                self.head = self.head.link
                return data
        else:
            data = before.link.data
            before.link = before.link.link
            return data

    def display(self):
        if not self.isEmpty():
            node = self.head
            while node != None:
                print(node.data, end="->")
                node = node.link
            print("None")
        else:
            print("None")

def linkedSum(head:linkedList):
    sum = 0
    node = head
    while node != None:
        sum += node.data
        node = node.link
    return sum

def inputInteger():
    ll = linkedList()
    count = int(input("노드의 갯수를 입력하세요"))
    for i in range(count):
        print("노드 %d 의 데이터" % (i + 1))
        data = int(input())
        ll.insert(i, data)
    ll.display()
    return ll


def pulsEnd(linklist: linkedList):
    n = int(input("리스트의 끝에 저장할 수를 입력하세요"))
    linklist.insert(linklist.size(), n)
    linklist.display()
    return linklist


def deletefinstNode(linkedLinst: linkedList):
    linkedLinst.delete(0)
    linkedLinst.display()

def valueCount(list:linkedList, value):
    count = 0
    node = list.head
    while node != None:
        if node.data == value:
            count +=1
        node = node.link
    print("%d 은 %d 번 들어있다." % (value, count))


list = linkedList()
for i in range(3):
    list.insert(i, i)
list.display()
valueCount(list,1)
# print(linkedSum(list.head))

# list.display()
# deletefinstNode(list)

# linklist = inputInteger()
# a = pulsEnd(linklist)
# linklist = inputInteger()
