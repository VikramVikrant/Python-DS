"""
This file is not running
"""
def BinarySearch(item,my_list):
    found=False
    first=0
    last=len(my_list)-1

    while ((first<= last) and found == False):
        mid= (first+last)//2

        if my_list[mid]== item:
            found=True
        else:
            if my_list[mid]<item:
                first=mid+1
            else:
                last=mid-1
    return found

l1=[12,23,34,45,56,67,89,90]
BinarySearch(45,l1)


