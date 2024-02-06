#rounds a number

# we need to be careful of round, as it rounds to the nearest even number
# eg, 4.5 rounds down to 4
# but 5.5 rounds up to 6
# so do not use if accuracy is essential
# Author: Michael Curley

numberToRound = float(input("Enter a float number: "))
roundedNumber = round(numberToRound)

print(" {} rounded is {}".format(numberToRound,roundedNumber))