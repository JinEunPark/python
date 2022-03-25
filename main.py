# 1
for i in range(1, 9):
    print("{} x 6 = {}".format(i, i * 6))

i = 1

while i < 10:
    print("{} x 6 = {}".format(i, (i * 6)))
    i += 1


# 2
def changeC_to_F(c):
    F = 32 + 1.8 * c
    return F


b = 32

print(changeC_to_F(b))

List = [1, 2, 3, 4]

for i in range(-1, -5, -1):
    print(List[i])


# 3
def sum_get(list):
    sum = 0
    for i in list:
        sum += i
    return sum


print(sum_get(List))

msg = "Data Structures in Python"
print(msg)
print(msg.lower())
print(msg.upper())

price = {'콩나물해장국': 4500, '갈비탕': 9000, '돈가스': 8000}

price['팟타이'] = 7000
price.update({'qkrw': 1212, 'rladlsrud': 13123})
print(price)

for i in price:
    price[i] -= 500

print(price)


def cirSum(n):
    if n == 1:
        return 1
    elif n > 1:
        return n + cirSum(n - 1)


print("순환함수 호출 결과: {}".format(cirSum(3)))


def momOnHat(i):
    if i == 1:
        return 1
    elif i > 1:
        return (1 / i) + momOnHat(i - 1)


print(momOnHat(3))


def bin_co(n, k):
    if k == 0 or k == n:
        return 1
    else:
        if 0 < k < n:
            return bin_co(n - 1, k - 1) + bin_co(n - 1, k)


print(bin_co(3, 1))


def factorial(n):
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum


def bin(n, r):
    return factorial(n) / factorial(n - r)


print(bin(10, 5))


def reverse(string):
    reverse_name = ''
    for i in string:
        reverse_name = i + reverse_name
    return reverse_name


String = "dosrnfivnsjerbgkjfbvsubtgqg"
print(reverse("sex"))


def revPrintNum(n):
    if n == 1:
        print(n, " ", end="")
        return
    elif n != 1:
        print(n, " ", end="")
        return revPrintNum(n - 1)


def PrintNum(n):
    if n != 1:
        PrintNum(n - 1)
        print(n, " ", end="")
        return
    elif n == 1:
        print(n, " ", end="")
        return


revPrintNum(9)
print("")
PrintNum(9)

global fabo
fabo = [0 for i in range(100)]

global count
count = 0


def fibonacci(n):
    global fabo
    fabo[n] += 1
    if n == 0:
        return 1
    elif n != 1:
        return fibonacci(n - 1), fibonacci(n - 2)


list = [1, 2, 3]
list[0] += 1
print(list)

fibonacci(10)
print(count)

print(fabo)


def tax(income):
    first = 1200- 1200 * 0.06
    second = 4600 - 4600 * 0.15
    third = 8800 - 8800 * 0.24
    forth = 15000 - 15000 * 0.35
    result = 0
    if income > 15000:
        result = forth + (income - 15000) * 0.62
    elif income > 8800:
        result = third + (income - 8800) * 0.65
    elif income > 4600:
        result = second + (income - 4600) * 0.76
    elif income > 1200:
        result = first + (income - 1200) * 0.85
    else:
        result = income - income * 0.06
    return result


print(tax(20000))
print(tax(1201))
print(tax(1199))
