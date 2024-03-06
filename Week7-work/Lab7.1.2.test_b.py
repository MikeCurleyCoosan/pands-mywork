# The with statement will automatically close the file when it is finished with it
# Author: Michael Curley
# Date: 06/03/2024

with open ("test_b.txt", "w") as f:
    data = f.write("test b\n") #Return the number of characters written to the file
    print(data)

with open ("test_b.txt", "w") as f2: #Open the file again. The file is overwritten
    data = f2.write("another line\n") #Again, return the number of characters written to the file
    print(data )
