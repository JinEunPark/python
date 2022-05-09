height = int(input("정수를 입력하세요"))
for i in range(0, height):
    print("    " * (height - i), end="  ")
    for e in range(0, i + 1):
        print(" {}".format(2 * e + 1), end="  ")
    for j in range(e, 0, -1):
        print(" {}".format(2 * j - 1), end="  ")
    print("    " * (height - i))
