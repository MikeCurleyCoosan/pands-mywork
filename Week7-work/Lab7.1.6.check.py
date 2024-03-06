#What happens is we run count.py or count2.py and the file count.txt does not exist?
# What happens if the file exists but is empty?
# What happens if the file contains something that is not an integer?
# What happens if the file contains a number?

# The file count.txt does not exist
# The program will throw an error

# The file exists but is empty
# The program will throw an error

# The file contains something that is not an integer
# The program will throw an error

# The file contains a number
# The program will run as expected

#Author: Michael Curley
#Date: 06/03/2024

#Lets create an itit program that will initialise the file and (if it doesn't exist) and write a 0 to it

import os.path

FILENAME = "count.txt" #The name of the file we will store the count in

if not os.path.isfile(FILENAME): #Check if the file exists
    write_number(0) #If it doesn't, create it and write a 0 to it

#Write a funttion that reads in a number from a file that already exists (count.txt)
def read_number():
    try:
        with open(FILENAME) as f: #Open the file for reading
            number = int(f.read()) #Read the number from the file
            return number #Return the number
    except IOError:
        return 0
    
#Write a function that takes in a number and overwrites a file (count.txt) with the number.
def write_number(number):
    with open(FILENAME, "wt") as f:
         #Write takes a string so we need to convert the number to a string
         f.write(str(number)) #Write the number to the file
