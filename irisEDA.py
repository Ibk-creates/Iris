import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load dataset
iris= pd.read_csv(r"C:\Users\OMT\Downloads\iris.csv")

# info about dataset
print(iris.head())
print(iris.describe())
print(iris.info())
print(iris.isnull().sum())

#summary statistics
print(iris.groupby('Species').agg({'SepalLengthCm': 'mean', 'SepalWidthCm': 'mean', 'PetalLengthCm': 'mean', 'PetalWidthCm': 'mean'}))

# visualization 
iris.hist(figsize=(10, 8))
plt.suptitle("Iris Dataset Histograms")
plt.show()

sns.boxplot(x='Species', y='SepalLengthCm', data=iris)
plt.title("Boxplot of Sepal Length by Species")
plt.show()

sns.scatterplot(x='SepalLengthCm', y='SepalWidthCm', hue='Species', data=iris)
plt.title("Scatter Plot of Sepal Length vs Sepal Width")
plt.show()

sns.pairplot(iris, hue='Species')
plt.suptitle("Pairplot of Iris Dataset", y=1.02)
plt.show()

sns.heatmap(iris.drop(columns='Species').corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap of Iris Dataset")
plt.show()