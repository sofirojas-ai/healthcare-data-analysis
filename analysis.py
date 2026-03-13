import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("heart.csv")

# Display first rows
print(data.head())

# Basic statistics
print(data.describe())

# Age distribution
data["age"].hist()
plt.title("Age Distribution of Patients")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
