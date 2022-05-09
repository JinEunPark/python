class Polynomia:

    def __init__(self):
        self.polyList = []

    def read_poly(self):

        high = int(input("최고차 항의 계수를 입력하세요"))

        for i in range(high+1):
            value = int(input("x^{} 의 계수를 입력하세요".format(i)))
            self.polyList.append(value)

    def degree(self):
        return self.polyList[-1]

    def evaluation(self):
        sum = 0
        for i in range(len(self.polyList)):
            if i == 0:
                sum += self.polyList[0]
            else:
                sum += self.polyList[i] ** i
        return sum

    def add(self, otherPoly):

        r_list = []
        self_lenght = len(self.polyList)
        other_lenght = len(otherPoly)

        if self_lenght >= other_lenght:

            for i in range(len(otherPoly)):
                r_list.append(self.polyList[i] + otherPoly[i])

            for e in range(other_lenght, self_lenght):
                r_list.append(self.ployList[e])
        else:
            for i in range(len(self.polyList)):
                r_list.append(self.otherPoly[i] + self.polyList[i])

            for e in range(self_lenght, other_lenght):
                r_list.append(otherPoly[e])

        return r_list

    def substract(self, otherPoly):

        r_list = []
        self_lenght = len(self.polyList)
        other_lenght = len(otherPoly)

        if self_lenght >= other_lenght:

            for i in range(len(otherPoly)):
                r_list.append(self.polyList[i] - otherPoly[i])

            for e in range(other_lenght, self_lenght):
                r_list.append(self.ployList[e])
        else:
            for i in range(len(self.polyList)):
                r_list.append(self.otherPoly[i] - self.polyList[i])

            for e in range(self_lenght, other_lenght):
                r_list.append(otherPoly[e])

        return r_list

    def multiply(self, otherPoly):

        lenght = len(self.polyList)+len(otherlist)-1

        r_list = [0 for x in range(lenght)]  # 최고차항을 가지는 리스트 생성
        for i in range(len(otherPoly)):
            for e in range(len(self.polyList)):
                r_list[i+e] += otherlist[i] * self.polyList[e]

        return r_list


ploy = Polynomia()
ploy.read_poly()
otherlist = [1,1]
print(ploy.multiply(otherlist))
