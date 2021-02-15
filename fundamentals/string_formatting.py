# String Formatting in Python
price = 49
quantity = 3
itemno = 567

txt = "The price is ${} dollars"
print(txt.format(price))

txt = "The price is ${:.2f} dollars"
print(txt.format(price))

myorder = "I want {}  pieces of item number {} for {:.2f} dollars"
print(myorder.format(quantity, itemno, price))