# Date: 29-Feb-2024
#Write a function that prints out a menu of commands we can perform, ie add
#view and quit. The function should return waht the user chose.

#The array we store the students in
students = []


# Display menu function, which displays a menu to the user 
def display_menu():
    print("What would you like to do?") # Print the menu
    print("\t(a) Add new student")  #Add a new studnet
    print("\t(v) View students")    #View all students
    print("\t(q) Quit")  #Quit
    choice = input("Type one letter (a/v/q):").strip()

    return choice

# The read_modules function which reads in the modules and the grades for each module for a given student
def read_modules():
    modules = [] # Create a new list to store the modules

    # Ask for the name of the first module (with leading and trailing whitespace removed)
    module_name = input("\tEnter the first module name (blank to quit): ").strip()
    #While the module_name is not blank, we can continue to read in each module and grade for the student
    while module_name != "":
        module = {} # Create a new dictionary to store the module name and grade
        module["name"] = module_name    # Store the module name
        module["grade"] = int(input("\tEnter grade: ")) # Store the grade (which we convert to an integer)
        modules.append(module) # Add the module to the list
        # Now read the next module name
        module_name = input("\tEnter next module name (blank to quit): ").strip()
    # Return the list of modules
    return modules

# The do_add function which allows the user to add a new student to the list of students
def do_add(students):
    # Create a new dictionary to store the student data
    current_student = {}
    # Ask the user for the student's name
    current_student["name"] = input("Enter name: ")
    # Ask the user for the student's modules and grades. Note: This calls the read_modules function which returns a list of modules
    current_student["modules"] = read_modules()
    # Add the student to the list of students and their modules
    students.append(current_student)

#test do_add function
'''
do_add(students)
do_add(students)
print(students)
'''

def do_view():
    #We'll fill this in later
    print("in viewing")

#Main program
#Call the display_menu function to display the menu and get the users choice
choice = display_menu()
#While the user's choice is not 'q', we and display the menu
while(choice != 'q'):
    #We could do this with lambda functions?? (Possibly coming later in the course? Just noting for now. May be worth looking into)

    if choice == 'a':
        do_add()    #Call the do_add function
    elif choice == 'v':
        do_view()   #Call the do_view function
    elif choice != 'q':
        print("\n\nPlease select either a, v or q") #If the user's choice is not 'a', 'v' or 'q', we again ask them for their choice
    choice = display_menu()

