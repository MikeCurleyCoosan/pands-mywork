# Date: 29-Feb-2024
#Write a function that prints out a menu of commands we can perform, ie add
#view and quit. The function should return waht the user chose.

# Define the function
def display_menu():
    print("What would you like to do?") # Print the menu
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice

def doadd():
    #We'll fill this in later
    print("in adding")

def doview():
    #We'll fill this in later
    print("in viewing")

#Main program
choice = display_menu()
while(choice != 'q'):
    #We could do this with lambda functions??

    if choice == 'a':
        doadd()
    elif choice == 'v':
        doview()
    elif choice != 'q':
        print("\n\nPlease select either a, v or q")
    choice = display_menu()

