# Plotting in Python Pandas
import pandas as pd
import os
import matplotlib.pyplot as plt

# Prepare Pathname
cwd = os.getcwd()
filename = "plotting.csv"
mytuple = (cwd, "pandas", filename)
path = "/".join(mytuple)

df = pd.read_csv(path)
df.plot()
plt.show()

df.plot(kind ='scatter', x = 'Duration', y = 'Calories')
plt.show()

df["Duration"].plot(kind='hist')
plt.show()