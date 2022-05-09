class priorityQueue:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return len(self.list) == 0

    def enqueue(self, item):
        self.list.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.list.pop([self.findmostBigIndex()])

    def findmostBigIndex(self):

        if self.isEmpty():
            return None
        else:

            maxIndex = 0
            for i in range(len(self.list)):
                if self.list[i] > self.list[maxIndex]:
                    maxIndex = i
            return maxIndex

    def peek(self):
        return self.list[self.findmostBigIndex()]

    def size(self):
        return len(self.list)

    def clear(self):
        self.list = []
