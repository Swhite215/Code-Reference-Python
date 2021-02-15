# Regex in Python
import re

# findall()
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# search()
y = re.search("ra", txt)
print(y)
print(y.start())
print(y.span())
print(y.string)
print(y.group())

z = re.split("\s", txt)
print(z)

b = re.split("\s", txt, 2)
print(b)

# sub()
c = re.sub("\s", "XX", txt)
print(c)