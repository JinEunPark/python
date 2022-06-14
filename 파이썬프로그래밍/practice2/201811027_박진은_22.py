# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# data_file = pd.read_csv("/Users/bagjin-eun/Documents/data_with_headers.numbers.cvs")
# time = data_file['time']
# time = time - time[0]
#
# sensors = data_file.loc[:,'s1','s4']
# print(sensors[0:6])
# avg_row = np.mean(sensors, 1)
# avg_col = np.mean(sensors, 0)
# result = pd.concat([time, sensors, avg_row], axis=1)
#
# plt.plot(time, sensors['s1'], 'r-', label='Sensor 2')
# plt.plot(time, avg_row,'b-',label='Average')
# plt.xlabel('Time (sec)')
# plt.ylabel('Sensor Values')
# plt.legend()
#
# plt.savefig('/Users/bagjin-eun/Desktop/201811027.pdf')

# a = (98+108+120)//14
# b = (-49 + 60)//14
# c = (108 + 60)//14
# d = (49 + 108 + 60)//14
# print(a,b,c,d)

