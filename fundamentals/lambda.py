# Lambdas in Python
x = lambda a: a + 10
print(x(5))

product = lambda x, y: x * y
print(product(10, 11))

def my_func(n):
    return lambda a: a * n

myTripler = my_func(3)
print(myTripler(10))
