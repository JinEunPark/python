def find_range_hozantal(hoz_list): # 수펑의 최솟값과 최댓값을 구하는 알고리즌 괄호로 탐색해서 최대와 최소를 찾는다.
    ldy = None
    rdy = None
    e = None
    for i in hoz_list:
        e = i.find("#")
        if e != -1:
            if ldy == None:
                ldy = e
            else:
                if ldy > e:
                    ldy = e

            for j in range(len(i)):
                if i[j] == "#" and rdy == None:
                    rdy = j
                elif i[j] == "#" and rdy != None:
                    if rdy < j:
                        rdy = j
    return (ldy, rdy+1) # 나를 한참이나 괴롭혔던거다


def find_range_Perpendicular(per_list): #수직 방향의 최솟값을 찾는 함수
    ldx = None
    rdx = None

    new = []
    for i in per_list:
        new.append(list(i))
    for e in range(len(new[0])):
        for i in range(len(new)):
            if new[i][e] == "#" and ldx == None:
                ldx = i
            elif new[i][e] == "#":
                if ldx > i:
                    ldx = i

            if new[i][e] == "#" and rdx == None:
                rdx = i
            elif new[i][e] == "#":
                if rdx < i:
                    rdx = i
    return (ldx, rdx+1)
wall = ["..........", ".....#....", "......##..", "...##.....", "....#....."]
def solution(wallpaper):
    lux = 0
    luy = 0
    rdx = 0
    rdy = 0
    luy, rdy = find_range_hozantal(wallpaper)
    lux, rdx = find_range_Perpendicular(wallpaper)
    answer = [lux, luy, rdx, rdy]
    return answer
print(solution(wall))