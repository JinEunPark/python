import linkedStack


class linkedList(linkedStack):
    def __init__(self):
        self.head = None

    def getNode(self, pos):
        if pos < 0:
            return None

        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node

        # rpos =0
        # while not rpos == pos and node != None:
        #     node = node.link
        #     rpos +=1
        # return node
        #

    def insert(self, pos, elem):
        before = self.getNode(pos - 1)
        if before == None:
            self.head = super.Node(elem, self.head)
        else:
            node = super.Node(elem, before.link)
            before.link = node

    def delete(self, pos):
        before = self.getNode(pos - 1)
        if before == None:
            if self.head is not None:
                self.head = self.haed.link
            elif before.link != None:
                before.link = before.link.link
# 자료구조 ㅈ됐다 시발