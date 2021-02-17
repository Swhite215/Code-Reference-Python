# Working with CSV in Pandas
import pandas as pd
import os

cwd = os.getcwd()
filename = "sample_employment_data.csv"
mytuple = (cwd, "pandas", filename)
path = "/".join(mytuple)

df = pd.read_csv(path)
print(df.to_string())
print(df)