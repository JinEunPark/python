from Dnode import Dnode


class doublelinkedDec:
    def __init__(self):
        self.rear = None
        self.front = None

    def isEmpty(self):
        return self.front == None

    def clear(self):
        self.front = self.front = None

    def size(self):
        if self.isEmpty():
            return 0
        else:
            count = 1
            dnode = self.front
            while dnode == self.rear:
                count += 1
                denode = denode.next
            return count

    def display(self):
        if self.isEmpty():
            print("None")
        else:
            denode = self.front
            while denode != self.rear:
                print(denode.data, end="->")
                denode = denode.next
            print(self.rear.data)

    def addFront(self, data):
        node = Dnode(data, None, self.front)  # link prev to front of instance
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.front.prev = node
            self.front = node

    def addRear(self, data):
        node = Dnode(data, self.rear, None)
        if self.isEmpty():
            self.rear = self.front = node
        else:
            self.rear.next = node
            self.rear = node

    def deleteFront(self):
        redata = self.front.data
        self.front = self.front.next

        if self.front == None:  # node가 하나밖에 없는거야
            self.front = self.rear = None
        else:
            self.front.prev = None
        return redata

    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.rear = self.front = None
            else:
                self.rear.next = None
            return data


doublelinkdec = doublelinkedDec()
for i in range(10):
    doublelinkdec.addRear(i)
doublelinkdec.display()
for i in range(3):
    doublelinkdec.deleteRear()
doublelinkdec.display()
