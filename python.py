import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


iris= pd.read_csv(r"C:\Users\OMT\Downloads\Iris.csv")
print(iris)
iris['SepalLengthCm'].hist()
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Distribution of Sepal Length')
plt.show()
plt.clf()
plt.plot(iris)
plt.show()/'