#A look at how to format strings in python
#Author: Michael Curley

#METHOD #1: Old Style Formatting
#Strings in Python have a unique built-in operation that can be accessed with the % operator.

name = 'Bob'
errorNo = 50159747054

print('Hello, %s' % name)# The s after the % denotes a string

print('%x' % errorNo) # The x after the % denotes hex number

#If you want to make multiple substitutions you need to wrap the right hand side of the argument in a tuple as shown below

print('Hello %s, there is an Ox%x error' %(name, errorNo))

#Also possible to refer to variable substitutions by name......using a mapping operator as below..

print('Hey %(name)s, there is a 0x%(errorNo)x error!' % {"name": name, "errorNo": errorNo })


#METHOD #2: New Style Formatting
# str.format style formatting

print('Hello, {}'.format(name))

#Multiple substitutions
print('Hey {}, there is a 0x{:x} error!'.format(name, errorNo))

#OR
print('Hey {name}, there is a 0x{errno:x} error!'.format(name=name, errno=errorNo))

#METHOD #3: String interpolation, string literals or f-strings

print(f'Hello, {name}')

a=5
b=10

print(f'Five and ten is {a+b} and not {(2 * (a+b))}')