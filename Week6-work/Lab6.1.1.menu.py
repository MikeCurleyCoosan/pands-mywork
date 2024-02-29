# Date: 25-Mar-2021
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

# test the function
choice = display_menu()
print(f"You chose { choice }")