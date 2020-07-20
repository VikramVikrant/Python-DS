from array import *
arr= array('u',[]) #array of characters
n=int(input("Enter the size of the array:"))

for i in range(0,n):
    x=input("Enter the next character:")
    arr.append(x)
print(arr)
for a in arr:
    print(a)
"""
Enter the size of the array:4
Enter the next character:a
Enter the next character:s
Enter the next character:d
Enter the next character:f
array('u', 'asdf')
a
s
d
f
"""
