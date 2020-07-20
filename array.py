from array import *
vals= array('i',[5,9,8,-6,89])
print(vals)
print("Address and size:",vals.buffer_info())
#Now to reverse a value
vals.reverse()
print("Reversed Array:",vals)

for i in vals:
    print(i,end='  ')

#now to work with characters
chars=array('u',['a','e','i'])
for a in chars:
    print("\n",a)