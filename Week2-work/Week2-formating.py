#Week2-Formatting
#Learning some python string formatting techniques
#Author: Michael Curley

#Example 1
price=49
txt = "The price is {:.2f} dollars" # .2f formats to two decimal places
print(txt.format(price)) #Formating txt string based on the information in the {}

#Example 2 Refering to multiple values
quantity=2
itemNo=456
price=49

myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity,itemNo, price)) #quantity is item 0, itemNo is item 1, and price is item 2

#Example 3 : Refering to same value more than once
age=23
name="John"

txt = "His name is {1}. {1} is {0} years of age."
print(txt.format(age, name)) # Here name is item 1, and age is item 0


#Example 4 : Named indexes

myOrder = "I have a {carname}, it is a {model}"
print(myOrder.format(carname = "Ford", model = "Mustang"))
