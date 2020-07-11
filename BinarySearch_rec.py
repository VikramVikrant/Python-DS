"""
Recursive Binary Search
"""
def BinarySearch(my_list,l,r,item):
    if r>=l:

        mid= l+(r-1)//2

        if my_list[mid] == item:  #if element is present in the middle itself
            return mid
        #if the item is smaller than the middle element
        elif my_list[mid] > item:                  #then it should be present in left sub array
            return  BinarySearch(my_list,l,mid-1,item)
        #if the element is larger than the middle element & it should be in the right subarray
        else:
            return BinarySearch(my_list,mid+1,r,item)

    else:
        return -1

my_list=[12,23,34,45,56]
item=23

result=BinarySearch(my_list,0,len(my_list)-1,item)

if result != -1:
    print ("Element is present at index % d" % result)

else:
    print ("Element is not present in array")



