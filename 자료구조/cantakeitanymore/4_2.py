import classStack

s = classStack.stack()


def checkstringPalindrome(string):
    string = string.lower()
    for i in string:
        s.push(i)
    for i in range(len(string)-1,-1,-1):
        print(i)
        if s.pop() == string[i]:
            continue
        else:
            return False
    return True
print(checkstringPalindrome("madam"))
