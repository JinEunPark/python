import numpy as np
import matplotlib.pyplot as plt

dataFile = np.genfromtxt("/Users/bagjin-eun/PycharmProjects/solveP/파이썬프로그래밍/practice/data_file.txt", delimiter=',')
time = dataFile[:, 0]
time = time - time[0]
print(time)

sensors = dataFile[:, 1:5]

avg = np.mean(sensors, axis=1)
mydata = np.hstack((time.reshape(1200, 1), sensors, avg.reshape(1200, 1)))
print(mydata)


plt.plot(time/60.0, sensors[:,0],'yo', label="Sensor1")
plt.plot(time/60.0, sensors[:,1],'ro', label="Sensor2")
plt.plot(time/60.0, sensors[:,2],'gx', label="Sensor3")
plt.plot(time/60.0, avg,'b.', label="average Sensors 1-4")

plt.legend()
plt.xlabel('Time(min)')
plt.ylabel('Sensors Values')
plt.title('PJE')
plt.savefig("/Users/bagjin-eun/Desktop/201811027PJE.pdf")