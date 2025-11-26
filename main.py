# Python Project - ECG dataset analysis
# Single ECG plot, ECG comparison, Statistics of normal vs abnormal ECG signals
# Biomedical Engineering related
# Alberto Rodríguez - @albertorgb21

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the data (obtained from Kaggle.com)
dataframe = pd.read_csv("data\ecg_data.csv")

# Check the shape of the dataframe
print(dataframe.shape)

# Separate the ECG signals from the labels
signals = dataframe.iloc[:, :-1].values
labels = dataframe.iloc[:, -1].values

# Plot any ECG signal (change index)
index = 21       # Pick between 0 and 4996
plt.figure(figsize=(12, 4))
plt.plot(signals[index])
plt.title(f'ECG - Patient {index} (Label: {labels[index]})')
plt.xlabel('Time Point')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

# ECG comparison
indexA = 10
indexB = 20
signalA = signals[indexA]
signalB = signals[indexB]
plt.figure(figsize=(12, 4))
plt.plot(signalA, label=f'Patient {indexA} (Label: {labels[indexA]})')
plt.plot(signalB, label=f'Patient {indexB} (Label: {labels[indexB]})')
plt.title(f'ECG Comparison - Patients {indexA} and {indexB}')
plt.xlabel('Time Point')
plt.ylabel('Amplitude')
plt.legend()  # This adds the legend
plt.grid(True)
plt.show()

# Label interpretation
count_0 = np.sum(labels == 0)
count_1 = np.sum(labels == 1)
print("Normal ECGs: ", count_0)
print("Abnormal ECGs: ", count_1)
print(f"Ratio Normal/Abnormal ECGs: {count_1/count_0:.3f}")
print(f"Percentage of Normal ECGs: {count_0/len(labels)*100:.2f}%")
print(f"Percentage of Abnormal ECGs: {count_1/len(labels)*100:.2f}%")
