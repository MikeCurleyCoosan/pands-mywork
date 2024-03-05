#The with statement will automatically close the file 
#when it is finished with it.

with open("test_a.txt", "r") as f:
    data = f.read()
    print(data)

#The old way of doing this 
    
#f = open("test_a.txt", "r")
#data = f.read()
#print(data)
#f.close()
    
