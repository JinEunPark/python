global a
a = 10
def draw_tree(row, left, right):
    if row == 0:
        return
    for i in range(left):
        print("-", end=" ")
    for j in range(0, row):
        print("X", end=" ")
    for e in range(right):
        print("-",end=" ")
    print()

    return draw_tree(row - 1, left // 2, right // 2),draw_tree(row - 1, left // 2, right // 2)


row = int(input())
draw_tree(row, 10, 10)
