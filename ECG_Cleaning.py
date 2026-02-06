import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

#Plotting the given data
df = pd.read_csv("Lab2_ecg.csv")

leadI = df['lead_I']
t = df['t']

#converting the data into arrays
time = np.array(t)
leadI = np.array(leadI)

#Finding the outlier data
mean = df['lead_I'].mean()
stnd = df['lead_I'].std()

series = pd.Series(leadI)

z_score = (series-mean)/stnd

outlier_i = z_score[abs(z_score)>1.5]
ecg = df['lead_I'].iloc[outlier_i.index].copy()
time2 = df['t'].iloc[outlier_i.index].copy()

print(ecg)

plt.plot(time,leadI)
plt.xlabel('time (s)')
#plt.show()


plt.plot(time2,ecg.head(1000))
plt.show()