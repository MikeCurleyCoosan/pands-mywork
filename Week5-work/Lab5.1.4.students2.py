#Write a program that will read in the data for the data structure above, ie reads in a students name,
# and then keeps reading in their modules and grades until the user enters a blank module name.
# The program should then print out the students name and their grades in each module.

modules = []
student = {}

student['name'] = input("Please Enter student's name: ")
courseName = input("Please enter the first course name (blank to quit): ")
grade = int(input("Please enter the first course grade (blank to quit): ")

while courseName != " ":
    modules.append({"courseName" : courseName, "grade" : grade})
    courseName = input("Please enter the next course name (blank to quit): ")
    if courseName != " ":
        grade = int(input("Please enter the next course grade (blank to quit): "))
    else: 
        break

student["modules"] = modules

print("Student: {}".format(student["name"]))    
for module in student["modules"]:
    print("\t{} \t: {}".format(module["courseName"], module["grade"]))