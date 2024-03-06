#Write a program that counts how many times it was run
#We will store the count in a file called count.txt. We are storing the count in a file so that it is not lost when the program ends.
#We would normally use a database for this kind of thing, but that is a more advanced topic.

#Author: Michael Curley
#Date: 06/03/2024

FILENAME = "count.txt" #The name of the file we will store the count in


#Write a funttion that reads in a number from a file that already exists (count.txt)
def read_number():
    with open(FILENAME) as f: #Open the file for reading
            number = int(f.read()) #Read the number from the file
            return number #Return the number
    
#Test it
num = read_number()
print(num)

#Write a function that takes in a number and overwrites a file (count.txt) with the number.
def write_number(number):
    with open(FILENAME, "wt") as f:
         #Write takes a string so we need to convert the number to a string
         f.write(str(number)) #Write the number to the file

#Test it
write_number(10)
