vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [[None, 29, None, None, None, 10, None],
          [29, None, 16, None, None, None, 15],
          [None, 16, None, 12, None, None, None],
          [None, None, 12, None, None, None, 18],
          [10, None, None, None, 27, None, None],
          [None, 15, None, 18, 25, None, None]]


def printAlledge(vertex, weight):

    for i in range(len(vertex)):
        for e in range(i, len(weight)):
            if weight[i][e] != None and weight != 0:
                print("(%c, %c %d)" % (vertex[i], vertex[e], weight[i][e]), end=" ")


printAlledge(vertex, weight)
print()
import numpy as np
array = np.array([1,2,3])
array2 = np.array([4,5,6])
array3 = np.vstack((array,array2))#파라미터의 전달을 튜플을 사용해서 하나의 변수로 만들어서 전달해야 한다.

print(array3)

array = np.random.normal(0,2,10)
array = array.reshape(2,-1)
print(array)

np.savetxt("/Users/bagjin-eun/PycharmProjects/solveP/자료구조/weigthGraph/save.txt",array,fmt="%f",delimiter=',')
import matplotlib.pyplot as plt

x = ["a", "b" ,"c", "d", "e", "f", "g"]
y = [1,2,3,4,5,6,7]
y2 = [24,14,51,24,12,5,0]
plt.plot(x,y, label='sold')
plt.plot(x,y2, label='onshalve')
plt.xlabel('alpabeet')
plt.ylabel('value')
plt.legend()
plt.show()