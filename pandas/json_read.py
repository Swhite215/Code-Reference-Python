# Working with JSON in Pandas
import pandas as pd
import os

cwd = os.getcwd()
filename = "sample_data.json"
mytuple = (cwd, "pandas", filename)
path = "/".join(mytuple)

df = pd.read_json(path)
print(df.to_string())
print(df)