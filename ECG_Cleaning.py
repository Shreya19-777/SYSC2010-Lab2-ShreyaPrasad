import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

#Unfiltered given data
df = pd.read_csv("Lab2_ecg.csv")
leadI = df['lead_I']
t = df['t']
time = np.array(t)
leadI = np.array(leadI)

#4.3.1 Plotting unfiltered data
#plt.plot(time,leadI)
plt.title('Lead I vs t')
plt.xlabel('time (s)')
plt.ylabel('lead I')
#plt.show()

#Finding mean and standard deviation
mean = df['lead_I'].mean()
stnd = df['lead_I'].std()

#4.3.2 ecg subset
ecg_subset = df.iloc[5000:10000].copy()
subset_data = ecg_subset.head(1000)
#plt.plot(subset_data['t'], subset_data['lead_I'])
plt.title('ECG susbset data')
plt.xlabel('time')
plt.ylabel('Subset lead_I')
#plt.show()

#4.3.6 Baseline Removal
subset_mean = np.mean(ecg_subset['lead_I'])
ecg_subset['lead_I_centered'] = ecg_subset['lead_I'] - subset_mean
#plt.plot(ecg_subset['t'], ecg_subset['lead_I_centered'])
plt.title('Centered Lead I vs t')
plt.xlabel('time (s)')
plt.ylabel('centered lead I')
#plt.show()

#choosing an odd and medium value so that you don't have a window size that is too large or too small
window_size = 7
smooth_signal = np.convolve(ecg_subset['lead_I_centered'],np.ones(window_size)/window_size,mode='same')
plt.plot(ecg_subset['t'], smooth_signal)
plt.title('Smoothed Signal')
plt.show()

'''
plt.plot(smooth_signal, label='Smoothed')
plt.plot(ecg_subset['lead_I_centered'], label='Original')
plt.title("Comparison of Smoothed vs Original Segment")
plt.legend()
plt.show()

'''
