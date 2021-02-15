import mymodule
from anothermodule import sum
import platform

a = mymodule.person1["name"]
mymodule.greeting(a)

sumValue = sum(1, 2)
print(sumValue)

x = platform.system()
y = dir(platform)
print(x)
print(y)