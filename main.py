import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

rawdata="student-mat.csv"

# https://www.geeksforgeeks.org/machine-learning/best-python-libraries-for-machine-learning/
df = pd.read_csv(rawdata, sep=";")

finalGrades=df["G3"].values

# Calculate summary stats
mean = np.mean(finalGrades)
median = np.median(finalGrades)
standardDeviation = np.std(finalGrades)

print(f"Summary stastics:\n\tMean: {mean}\n\tMedian: {median}\n\tStandard Deviation: {standardDeviation}")

#https://realpython.com/python-seaborn/
# https://seaborn.pydata.org/tutorial/distributions.html
# generate graphs
sns.set_theme()
histogram = sns.displot(data=df, x="G3")
#plt.show()
# https://stackoverflow.com/a/34796529
plt.savefig("histogram.png")
