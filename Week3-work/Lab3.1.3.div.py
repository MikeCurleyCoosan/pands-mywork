# program that reads in two numbers and
# outputs the integer answer and remainder

x = int(input("Enter your number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x//y) # // gives the answer as an int
remainder = x%y # % gives the remainder

print("{} divided by {} is {} with a remainder of {}".format(x, y, answer, remainder))
