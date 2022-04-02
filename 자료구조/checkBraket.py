class stack:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)

    def clear(self):
        self.list = []  # restatement

    def push(self, item):
        self.list.append(item)

    def pop(self):
        self.list.pop(-1)

    def peek(self):
        return self.list[-1]


def checkBraket(string):
    s = stack()

    for i in string:

        if i in '([{':
            s.push(i)
        elif i in ')]}':

            ch = s.pop()

            if (ch == '(' and i == ')') or (ch == '[' and i == ']') or (ch == '{' and i == '}'):
                continue
            else:
                return False
    if s.size == 0:
        return True
    else:
        return False


string = '(10 +10)-[10101]19293n4e['
print(checkBraket(string))
string2 = '[12[121212[121]123]123[12]12[12]12[]1]'
print(checkBraket(string2))
