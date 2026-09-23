import pandas as pd
import numpy as np

rawdata="student-mat.csv"

# https://www.geeksforgeeks.org/machine-learning/best-python-libraries-for-machine-learning/
df = pd.read_csv(rawdata, sep=";")

finalGrades=df["G3"].values

mean = np.mean(finalGrades)
median = np.median(finalGrades)
standardDeviation = np.std(finalGrades)

print(f"Summary stastics:\n\tMean: {mean}\n\tMedian: {median}\n\tStandard Deviation: {standardDeviation}")