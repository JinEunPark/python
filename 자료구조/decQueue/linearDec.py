class linearDec:
    def __init__(self):
        self.list = []
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return len(self.list) == 0

    def addFront(self, item):
        self.list.insert(0, item)

    def deleteFront(self):
        return self.list.pop(0)

    def deleteFront(self):
        self.list.pop(-1)

    def addRear(self, item):
        self.list.append(item)

    def deleteRear(self):
        return self.list.pop(-1)

    def clear(self):
        self.list = []

    def size(self):
        return len(self.list)


def define_palindrome(string):
    dec = linearDec()
    dec2 = linearDec()
    for i in string:
        dec.addRear(i)  # 문자하나하나 삽입한다.

    for e in range(len(string)//2):
        dec2.addFront(dec.deleteFront())


    for j in range(len(dec2.list)):
        if dec.deleteRear() == dec2.deleteRear():
            continue
        else:
            return False
    return True


print(define_palindrome("qkrwlsdms"))
