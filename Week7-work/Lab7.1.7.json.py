#Write a function that will store a simple Dict to a file as JSON. Test the function by storing the Dict d to a file called testdict.json.

#Author: Michael Curley
#Date: 06/03/2024

import json

FILENAME = "testdict.json" #The name of the file we will store the Dict in
sample = dict(name="Fred", age=31, grades=[67, 78, 90]) #Create a sample Dict

def write_dict(obj):
    with open(FILENAME, "wt") as f:
        json.dump(obj, f) #Write the Dict to the file

#Test it

write_dict(sample) #Write the Dict to the file