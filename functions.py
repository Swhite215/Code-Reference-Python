def add(x, y):
    sum = x + y
    return sum

def multi_args(**kwargs):
    print("His last name is " + kwargs["lname"])

def func_default(country = "U.S.A"):
    print("I am from " + country)

def display_list(foods):
    for food in foods:
        print(food)

sum = add(1, 3)
print(sum)

concatenate = add("Spencer", " White")
print(concatenate)

multi_args(fname = "Spencer", lname = "White")

func_default()
func_default("Morocco")

fruit = ["apple", "banana", "cherry"]
display_list(fruit)

def tri_recursion(k):
    print(k)
    if (k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

tri_recursion(6)