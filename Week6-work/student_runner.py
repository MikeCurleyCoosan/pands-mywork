#Date: 29:02:2024
#Author: Michael Curley
#Demonstrating modules with student_util.py and student_runner.py

import student_util as su #Import the student_util module and give it the alias su

students = [] #The array we store the students in

#Main program
students = [] #The array we store the students in
choice = su.display_menu() #Call the display_menu function and store the result in the variable choice
while choice != "q": #While the user's choice is not q
    if choice in su.choice_map: #If the user's choice is in the choice_map dictionary
        su.choice_map[choice](students) #Call the function that the user's choice maps to and pass in the list of students as a parameter
    else:
        print("Please select either a,v or q") #If the user's choice is not in the choice_map dictionary, print an error message
    choice = su.display_menu()