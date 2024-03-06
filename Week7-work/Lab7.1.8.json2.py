#Write a function that will read a Dict object from a file. Test the function by reading the Dict from the file testdict.json.

#Author: Michael Curley
#Date: 06/03/2024

import json

FILENAME = "testdict.json" #The name of the file we will store the Dict in

def read_dict(): #This will throw an error if the file does not exist. It should readly just return an empty Dict. We will fix this later.
    with open(FILENAME) as f: #Open the file for reading
        return json.load(f)

#Test it
somedict = read_dict()
print(somedict) #Print the Dict