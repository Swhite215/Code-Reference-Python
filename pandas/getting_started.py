import pandas as pd

# Print Version
print(pd.__version__)

# Create a Dataset
mydataset = {'cars': ["BMW", "Volvo", "Ford"], 'pasings': [3,7,2]}

# Create a Data Frame
myvar = pd.DataFrame(mydataset)

# Print Data Frame
print(myvar)

# Series - A Panda Series is like a column in a table, it is a one-dimensional array holding data of any type
a = [1, 7, 2]

# Create Series from List with Custom Indices
myseries = pd.Series(a, index = ["x", "y", "z"])

print(myseries)
print(myseries["x"])
print(myseries[1])
print(myseries[2])

# Create Series from Dict
calories = {"day1": 420, "day2": 380, "day3": 390}
mysecondseries = pd.Series(calories)
print(mysecondseries)

# DataFrames
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# Create Data Frame with Custom Indices
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
print(df.loc["day1"]) # Print First Row
print(df.loc[["day1", "day2"]]) # Print First and Second Rows