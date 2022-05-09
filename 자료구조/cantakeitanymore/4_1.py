class Stack:
    def __init__(self):
        self.top = []

    def pop(self):
        if len(self.top) != 0:
            return self.top.pop(-1)

    def push(self, item):
        self.top.append(item)

    def clear(self):
        self.top = []

    def size(self):
        return len(self.top)

    def __str__(self):
        return str(self.top)


s = Stack()
string = input("dlqfur")
s.push(1)
print(s.pop())

for i in range(len(string)):
    s.push(string[i])
for e in range(len(string)):
    t = s.pop()
    print(t, end="")
