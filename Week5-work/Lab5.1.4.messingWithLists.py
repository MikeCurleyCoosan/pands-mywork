#Messing with lists
#Author: Michael Curley

#Lists that have the same elements but in different orders are not equal

a = ["apple", "banana", "cherry"]

b = ["cherry", "apple", "banana"]

print(a == b) #False

#List elements can be accessed by index

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

print(a[0]) #foo
print(a[2]) #bax
print(a[5]) #corge

#Negative indices count from the end of the list

print(a[-1]) #corge
print(a[-2]) #quux
print(a[-6]) #foo

#Slicing also works with lists. If a is a list, the expression a[m:n] returns the portion of a from index m to, but not including, index n

b = a[1:4] #['bar', 'baz', 'qux']
print(b)
#Both positive and negative indices can be sliced

c = a[-5:-2] #['bar', 'baz', 'qux']
print(c)

print(b == c) #True

#To reverse a list, use the slice a[::-1]

print(a[::-1]) #['corge', 'quux', 'qux', 'baz', 'bar', 'foo']

#If you use the [::] slice, you return a copy of the list (shallow copy)
d = a[::]

print(d) #['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

print(a is d) #False
print(a == d) #True

#If you use the slice [::2], you return every second element of the list
e = a[::2]  
print(e) #['foo', 'baz', 'quux']

#Several python operators can be used with lists, including the + operator for concatenation and the * operator for repetition

f = a + ['grault', 'garply'] #['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'grault', 'garply']
print(f)

g = a * 2 #['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(g)

#We can use the in and not in operators to check if a list contains a specific value

print('qux' in a) #True
print('thud' not in a) #True
print('thud' in a) #False

#The len() function returns the number of elements in a list

print(len(a)) #6

#The min() and max() functions return the smallest and largest elements of a list, respectively

print(min(a)) #bar
print(max(a)) #qux

#Lists can be nested within othe lists

x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']

print(x[0], x[2], x[4]) #a g j
