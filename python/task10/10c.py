import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("students.csv")

# x-axis = student names
x = df["Name"]

# Plot each test as a separate line
plt.plot(x, df["Test1"], marker='s', label="Test1")
plt.plot(x, df["Test2"], marker='o', label="Test2")
plt.plot(x, df["Test3"], marker='*', label="Test3")
plt.plot(x, df["Test4"], marker='x', label="Test4")

plt.ylabel("Marks")
plt.title("Student Marks Across Tests")
plt.legend()
plt.show()
