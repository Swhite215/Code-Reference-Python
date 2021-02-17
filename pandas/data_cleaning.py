# Data Cleaning
import pandas as pd
import os

# Prepare Pathname
cwd = os.getcwd()
filename = "dirtydata.csv"
mytuple = (cwd, "pandas", filename)
path = "/".join(mytuple)

# Remove Rows with Empty Cells
df = pd.read_csv(path)
new_df = df.dropna()

print(new_df)

# Replace Empty Values in Entire DataFrame
df.fillna(130, inplace = True)

## Replace Empty Values in Columns
df["Calories"].fillna(130, inplace = True)

# Replace Using Mean, Median, or Mode
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)

y = df["Calories"].median()
df["Calories"].fillna(y, inplace = True)

z = df["Calories"].median()
df["Calories"].fillna(z, inplace = True)

# Cleaning Wrong Format - Convert To Datetime
df["Data"] = pd.to_datetime(df["Data"])
df.dropna(subset=["Data"], inplace = True)

# Cleaning Wrong Data - Replacing Values
df.loc[7, 'Duration'] = 45

# Replace Values Based on Rule
for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.loc[x, 'Duration'] = 120

# Remove Rows Based on Rule
for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.drop(x, inplace = True)

# Remove Duplicatesx - Discover and Drop
print(df.duplicated())
df.drop_duplicates(inplace = True)

