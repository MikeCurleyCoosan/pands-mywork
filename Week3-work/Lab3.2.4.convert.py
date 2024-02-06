#Question : I am writing an application at the moment, in it I take an input of an amoutn in the form
# -9.44(9 dollars and 44 cents). The issues is there may or may not be a minus sign, and the bank takes
#the amound in cent(944). Write a program called convert.py that takes in a float amoung of dollars
#and returns that absolute amount in cent

#Author: Michael Curley

bankFloat = (input("Please enter an amount: "))

absoluteBank = abs(bankFloat)

returnedValue = int(absoluteBank * 100)

print(" That amount in cents is : {} cents".format(returnedValue))