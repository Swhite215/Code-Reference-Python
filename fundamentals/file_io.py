# File I/O in Python
import os

# Get Path
filename = "demofile.txt"
cwd = os.getcwd()
mytuple = (cwd, "fundamentals", filename)
path = "/".join(mytuple)

# open(filename, mode) - modes - read, append, write, create
f = open(path, "r")
print(f.read()) # Returns Whole Text

f.close()

filenametwo = "heroes.txt"
newtuple = (cwd, "fundamentals", filenametwo)
pathTwo = "/".join(newtuple)
f2 = open(pathTwo, "a")

f2.write("Armadias is loyal.\n")
f2.write("Tranquility is a Luxin.\n")
f2.write("Flare is fierce.\n")
f2.close()

if os.path.exists(pathTwo):
    os.remove(pathTwo)
else:
    print("The file does not exist!")