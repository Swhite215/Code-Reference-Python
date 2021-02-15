# Iterators in Python

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myItTwo = iter(mystr)

print(next(myItTwo))
print(next(myItTwo))
print(next(myItTwo))
print(next(myItTwo))
print(next(myItTwo))
print(next(myItTwo))

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

