# Strings in Python
a = "Hello"
b = "World"
print(a + " " + b)

c = """ Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""

print(c)

# Strings are Arrays
name = "Spencer White"
print(name[0])
print(len(name)) # Length
print("White" in name) # Check for Substring
print("Michael" not in name)

if "White" in name:
    print("White is in the name")

if "Michael" not in name:
    print("Michael is not in the name")

for x in name:
    print(x)

# Slicing Strings
print(name[0:7]) # Prints Spencer
print(name[:7]) # Prints Spencer
print(name[8:]) # Prints White

# Modifying Strings
print(name.upper())
print(name.lower())
print("  TEST  ".strip())
print(name.replace("White", "Elgin"))
print(name.split(" "))

# Format Strings
age = 27
txt = "My name is " + name + " and I am {}"
print(txt.format(age))

# Escape Characters
print("We are the \"Luxin\"!")

# Methods
capitalLetter = name.capitalize()
lowerCase = name.casefold()
centered = name.center(10)
count = name.count("e")
encoded = name.encode()
endsWith = name.endswith(".")
find = name.find("hit")
index = name.index("hit")

# Checks
print(name.isalnum())
print(name.isalpha())
print(name.isdecimal())
print(name.isdigit())
print(name.islower())
print(name.isnumeric())
print(name.isprintable())
print(name.isspace())
print(name.istitle())
print(name.isupper())

myTuple = ("Armadias", "Von", "Elgin")
print(" ".join(myTuple))