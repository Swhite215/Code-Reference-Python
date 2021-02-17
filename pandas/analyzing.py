import pandas as pd
import os

cwd = os.getcwd()
filename = "sample_data.json"
mytuple = (cwd, "pandas", filename)
path = "/".join(mytuple)

df = pd.read_json(path)

# Head - Returns Headers and # of Rows from Top
print(df.head(10))

# Tail - Returns Header and # of Rows from Bottom
print(df.tail())

# Info - Givers Information About Dataset - Rows, Columns, Column Name + Data Type, Nulls
print(df.info())