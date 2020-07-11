"""
Iterative binary search
l=first element of the list
r=last element of the list
"""

def binarySearch(my_list,l,r,item):
    while l<=r:
        mid=(l+(r-1))//2


        if my_list[mid]==item:
            return  mid
        elif my_list[mid]<item:
            l=mid+1
        else:
            r=mid-1

    return -1

my_list=[12,23,34,45,56,67,89,90]
item=89

result=binarySearch(my_list,0,len(my_list)-1,item)

if result!=-1:
    print("Element is present at index % d. " %result)
else:
    print("Element is not present in the list.")


