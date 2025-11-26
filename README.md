# ECG-Dataset-Analysis
Basic analysis of ECG Dataset obtained from Kaggle.
Dataset Information:
  This dataset contains the ECG readings of patients. Each row corresponds to a single complete ECG of a patient. Every single ECG is composed of 140 data points(readings).
  Columns:- 1)Columns 0-139 contain the ECG data point for a particular patient. These are floating point numbers.
  2)The label which shows whether the ECG is normal or abnormal. It is a categorical variable with value eiteither 0 or 1.
Dataset link: https://www.kaggle.com/datasets/devavratatripathy/ecg-dataset/data

Code:
- Load data from dataset. Separate signals from labels
- Plot single ECG signal.
- Comparative plot of 2 ECG signals.
- Basic label-related statistics.
