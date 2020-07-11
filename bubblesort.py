def bubble_sort(my_list):
    swap_again=True
    n=len(my_list)
    while n>0 and swap_again == True:
        n=n-1
        swap_again=False

        for i in range(n):
            if my_list[i]>my_list[i+1]:
                my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
                swap_again=True

    return my_list

my_list=[23,12,11,45,34,11,90,21]
print(bubble_sort(my_list))