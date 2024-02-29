# 29-Feb-2024
#Author: Michael Curley
#Write a program that stores a students name and a list of their modules and grades in a dictionary.
#The program should allow the user to add new students and to view the current list of students and their modules and grades.

#The program should continue to run until the user chooses to quit.

#The program should use functions to allow the user to add a new student and view all students.

students = []

def display_menu():
    print("What would you like to do?") # Print the menu
    print("\t(a) Add new student")  #Add a new studnet
    print("\t(v) View students")    #View all students
    print("\t(q) Quit")  #Quit
    choice = input("Type one letter (a/v/q):").strip()

    return choice

def do_add(students):
    current_student = {}
    current_student["name"] = input("Enter name: ")
    current_student["modules"] = read_modules()
    students.append(current_student)

def read_modules():
    modules = []
    module_name = input("\tEnter the first module name (blank to quit): ").strip()
    while module_name != "":
        module = {}
        module["name"] = module_name
        module["grade"] = int(input("\tEnter grade: "))
        modules.append(module)
        module_name = input("\tEnter next module name (blank to quit): ").strip()
    return modules

def do_view(students):
    for current_student in students:
        print(current_student["name"])
        display_modules(current_student["modules"])


def display_modules(modules):
    print("\tName \tGrade")
    for module in modules:
        print(f"\t {module['name']}\t{module['grade']}")

def do_nothing(dummy):
    pass

choice_map = {
    "a": do_add,
    "v": do_view,
    "q": do_nothing
}

#Main program
students = []
choice = display_menu()
while choice != "q":
    if choice in choice_map:
        choice_map[choice](students)
    else:
        print("Please select either a,v or q")
    choice = display_menu()
