#Date: 29:02:2024
#Author: Michael Curley
#Demonstrating modules with student_util.py and student_runner.py

from github import Github
import json

FILENAME = "studentsData.json" #The name of the file we will store the students in


#display_menu function, which displays a menu to the user
def display_menu():
    print("What would you like to do?") # Print the menu
    print("\t(a) Add new student")  #Add a new studnet
    print("\t(v) View students")    #View all students
    print("\t(s) Save students")    #Save students to file.....Modification from week 7 work
    print("\t(q) Quit")  #Quit
    choice = input("Type one letter (a/v/q):").strip()

    return choice

#do_add function which allows the user to add a new student to the list of students
def do_add(students): #The function takes in the list of students as a parameter
    current_student = {} # Create a new dictionary to store the student data
    current_student["name"] = input("Enter name: ") # Ask the user for the student's name and store it in the dictionary as the value for the key "name"
    current_student["modules"] = read_modules() # Ask the user for the student's modules and grades. Note: This calls the read_modules function which 
                                                #returns a list of modules
    students.append(current_student) # Add the student to the list of students and their modules

#The read_modules function which reads in the modules and the grades for each module for a given student
def read_modules():
    modules = []    # Create a new list to store the modules
    module_name = input("\tEnter the first module name (blank to quit): ").strip() # Ask for the name of the first module (with leading and trailing whitespace removed)
    while module_name != "":    #While the module_name is not blank, we can continue to read in each module and grade for the student
        module = {} # Create a new dictionary to store the module name and grade
        module["name"] = module_name # Store the module name as a value for the key name    
        module["grade"] = int(input("\tEnter grade: ")) # Store the grade (which we convert to an integer) as a value for the key grade
        modules.append(module) # Add the module to the list
        module_name = input("\tEnter next module name (blank to quit): ").strip() # Now read the next module name
    return modules

#do_view function which allows the user to view all students currently stored in the list of students
def do_view(students): #The function takes in the list of students as a parameter
    for current_student in students: #For each student in the list of students
        print(current_student["name"]) #Print the student's name which is stored as the value for the key "name" in the dictionary
        display_modules(current_student["modules"]) #Call the display_modules function which takes in the list of modules for the student as a parameter, 
                                                    #this function will print out the modules and grades for the student


#display_modules function which takes in a list of modules and grades for a student and prints them out
def display_modules(modules):   #The function takes in the list of modules as a parameter
    print("\tName \t\tGrade")
    for module in modules:
        print(f"\t{module['name']}\t\t{module['grade']}")

#do_save function which takes in the list of students and saves them to a file
def do_save(students)
    #We will put the call to save dictionary object here
    write_dict(students) #Modification from week 7 work
    print("students saved to file ")

def write_dict(obj):
    with open(FILENAME, "wt") as f:
        json.dump(obj, f) #Write the Dict to the file


#do_nothing function which takes in a dummy parameter and does nothing
def do_nothing(dummy):
    pass

#the choice_map dictionary which maps a letter to a function
choice_map = {
    "a": do_add,
    "v": do_view,
    "s": do_save, #Modification from week 7 work
    "q": do_nothing
}