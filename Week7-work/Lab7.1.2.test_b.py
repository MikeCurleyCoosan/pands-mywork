# The with statement will automatically close the file when it is finished with it
# Author: Michael Curley
# Date: 06/03/2024

with open ("test_b.txt", "w") as f:
    data = f.write("test b\n")
    print(data)
