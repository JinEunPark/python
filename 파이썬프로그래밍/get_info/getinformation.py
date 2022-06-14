import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_file= pd.read_csv("/Users/bagjin-eun/Downloads/data_with_headers.csv")
time = data_file['time']
time=time-time[0]

sensors = data_file.loc[:,'s1':'s4']

avg_row=np.mean(sensors,1)

result = pd.concat([time,sensors,avg_row],axis=1)

result.to_csv('/Users/bagjin-eun/Desktop/result/result.csv')
# result.to_excel('/Users/bagjin-eun/Desktop/result/result.xlsx')
result.to_html('/Users/bagjin-eun/Desktop/result/result.htm')

plt.plot(time,sensors['s1'],'r-',label='Sensor 2')
plt.plot(time,avg_row,'b.',label='Average')

plt.xlabel('Time(sec)')
plt.ylabel('Sensor Values')
plt.legend()
plt.savefig('python_data.pdf')