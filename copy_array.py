from array import *
value=array('i',[23,45,-89,56,49,90,13])
print(value.buffer_info())
#Creating new array
newArr= array(value.typecode,(a for a in value))
##We use typecode when we don't know the value we are copying
for e in newArr:
    print(e,end=' ')
"""
(54903168, 7)
23 45 -89 56 49 90 13 
"""
