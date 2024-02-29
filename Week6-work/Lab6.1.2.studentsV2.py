# 29-Feb-2024
#Author: Michael Curley
#Write a program that stores a students name and a list of their modules and grades in a dictionary.
#The program should allow the user to add new students and to view the current list of students and their modules and grades.

#The program should continue to run until the user chooses to quit.

#The program should use functions to allow the user to add a new student and view all students.

students = [] #The array we store the students in

#display_menu function, which displays a menu to the user
def display_menu():
    print("What would you like to do?") # Print the menu
    print("\t(a) Add new student")  #Add a new studnet
    print("\t(v) View students")    #View all students
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
    print("\tName \tGrade")
    for module in modules:
        print(f"\t {module['name']}\t{module['grade']}")

#do_nothing function which takes in a dummy parameter and does nothing
def do_nothing(dummy):
    pass

#the choice_map dictionary which maps a letter to a function
choice_map = {
    "a": do_add,
    "v": do_view,
    "q": do_nothing
}

#Main program
students = [] #The array we store the students in
choice = display_menu() #Call the display_menu function and store the result in the variable choice
while choice != "q": #While the user's choice is not q
    if choice in choice_map: #If the user's choice is in the choice_map dictionary
        choice_map[choice](students) #Call the function that the user's choice maps to and pass in the list of students as a parameter
    else:
        print("Please select either a,v or q") #If the user's choice is not in the choice_map dictionary, print an error message
    choice = display_menu()
