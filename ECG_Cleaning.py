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
'''
#plt.plot(ecg_subset['t'], ecg_subset['lead_I_centered'])
plt.title('Centered Lead I vs t')
plt.xlabel('time (s)')
plt.ylabel('centered lead I')
#plt.show()
'''

#4.3.7 Smoothing the signal using a window size of 7
window_size = 7
smooth_signal = np.convolve(ecg_subset['lead_I_centered'],np.ones(window_size)/window_size,mode='same')
'''
plt.plot(ecg_subset['t'], smooth_signal)
plt.title('Smoothed Signal')
plt.xlabel('Time')
plt.ylabel('Smoothed Lead_I')
plt.show()
'''

plt.plot(ecg_subset['t'][0:500], ecg_subset['lead_I_centered'].values[0:500], label='Original')
plt.plot(ecg_subset['t'][0:500], smooth_signal[0:500], label='Smoothed')
plt.title("Comparison of Smoothed vs Original Segment")
plt.legend()
plt.show()

processed_df = pd.DataFrame({'time': ecg_subset['t'],'lead_I': smooth_signal})
processed_df.to_csv("processd_ecg.csv", index=False)
