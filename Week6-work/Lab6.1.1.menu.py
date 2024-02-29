# Date: 29-Feb-2024
#Write a function that prints out a menu of commands we can perform, ie add
#view and quit. The function should return waht the user chose.

students = []


# Define the function
def display_menu():
    print("What would you like to do?") # Print the menu
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice

def read_modules():
    modules = []
    module_name = input("\tEnter the first module name (blank to quit): ").strip()

    while module_name != "":
        module = {}
        module["name"] = module_name
        module["grade"] = int(input("\tEnter grade: "))
        modules.append(module)
        # Now read the next module name
        module_name = input("\tEnter next module name (blank to quit): ").strip()
    return modules


def do_add(students):
    current_student = {}
    current_student["name"] = input("Enter name: ")
    current_student["modules"] = read_modules()
    students.append(current_student)

#test do_add function
do_add(students)
do_add(students)
print(students)

def do_view():
    #We'll fill this in later
    print("in viewing")

#Main program
choice = display_menu()
while(choice != 'q'):
    #We could do this with lambda functions??

    if choice == 'a':
        do_add()
    elif choice == 'v':
        do_view()
    elif choice != 'q':
        print("\n\nPlease select either a, v or q")
    choice = display_menu()

