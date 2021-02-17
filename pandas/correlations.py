# Correlation in Python Pandas
import pandas as pd
import os

# Prepare Pathname
cwd = os.getcwd()
filename = "correlations.csv"
mytuple = (cwd, "pandas", filename)
path = "/".join(mytuple)

df = pd.read_csv(path)
print(df.corr())

# Correlations - How Columns Compare to One Another
    # High Correlation 0.6 to -0.6
    # Perfect Correlation 1.0 (Directly Proportional) or -1.0 (Inversely Proportional)
