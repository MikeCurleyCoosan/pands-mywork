#Give the absolute value of a number

#Question : Write a program (absolute.py) that takes in a number and gives its absolute value
#(i.e. -4.0 or 4.0 would both output 4)

#In the question, number is ambiguous but the output implies that we should be dealing with
#floats, so here we are casting the input to a float

number = float(input("Enter a number: "))
absoluteValue = abs(number)

print("The absolute value of {} is {}".format(number, absoluteValue))
