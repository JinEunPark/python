class linearQueue:
    MAXQ = 10

    def __init__(self):
        self.list = []

    def isEmpty(self):
        return len(self.list) == 0

    def enqueue(self, item):
        self.list.append(item)  # 항목의 삽인은 뒤에서만 일어난다.

    def dequeue(self):
        if self.isEmpty() == False:
            return self.list.pop(0)  # 항목의 반환은 앞쪽에서만 일어난다.

    def peek(self):
        if self.isEmpty() == False:
            return list[0]

    def size(self):
        return len(self.list)

    def clear(self):
        self.list = []
