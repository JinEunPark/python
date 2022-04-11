from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def clear(self):
        self.head = None

    def size(self):
        node = self.head
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count

    def display(self, msg="LinkedList : "):
        print(msg, end='')
        node = self.head
        while not node == None:
            print(node.data, end=' -> ')
            node = node.link
        print('None')

    def getNode(self, pos):
        if pos < 0: return None
        node = self.head
        #         rpos = 0
        #         while not rpos == pos and node!=None:
        #             node = node.link # rpos =0, node -> 0,1
        #             rpos+=1 # rpos =1
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node

    def insert(self, pos, elem):
        before = self.getNode(pos - 1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            before.link = Node(elem, before.link)

    def delete(self, pos):

        before = self.getNode(pos - 1)

        if before == None:
            if self.head is not None:
                self.head = self.head.link
        else:
            before.link = before.link.link


def reverse(head):
    ahead = head.head
    prev = None
    while ahead != None:
        garbage = prev
        prev = ahead
        ahead = ahead.link
        prev.link = garbage
    reversLinkedlist = LinkedList()
    reversLinkedlist.head = prev
    return reversLinkedlist


original = LinkedList()
for i in range(5):
    original.insert(i, i * 10)
original.display()
print(original.head.link.data)
reverseLikedList = reverse(original)
reverseLikedList.display()
