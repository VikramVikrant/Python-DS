def linSearch(item,my_list):
    i=0
    found=False

    while i<len(my_list) and found==False:
        if my_list[i]==item:
            found=True
        else:
            i=i+1
    return found

test=[56,67,34,12,37,56,67,78,98]
print(linSearch(67,test))
print(linSearch(99,test))

