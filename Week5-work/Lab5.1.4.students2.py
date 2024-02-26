#Write a program that will read in the data for the data structure above, ie reads in a students name,
# and then keeps reading in their modules and grades until the user enters a blank module name.
# The program should then print out the students name and their grades in each module.
# The program should use a list of dictionaries to store the data. A sample input session might look like this:

#Enter the students name: Mary
#Enter the name of the module: Programming
#Enter the grade for Programming: 45
#Enter the name of the module: History
#Enter the grade for History: 99
#Enter the name of the module:

#Mary
#        Programming : 45
#        History : 99

name = input("Enter the students name: ")
modules = []
student = {}

student["name"] = name

courseName = str(input("Enter the name of the module: "))
while courseName != "":
    module = {}
    module["courseName"] = courseName
    module["grade"] = int(input("Enter the grade for {}: ".format(courseName)))
    modules.append(module)
    student["modules"] = modules
    module = {}
    courseName = input("Enter the name of the module: ")

print("Student: {}".format(student["name"])) 
for module in student["modules"]:
    print("\t{} \t: {}".format(module["courseName"], module["grade"]))
