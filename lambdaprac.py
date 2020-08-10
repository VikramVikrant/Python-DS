from functools import reduce

no = [2,3,5,7,8,9,11,13,12,23,25,34,36,38]
even = list(filter(lambda n: n%2 == 0,no))#filter is used to filter the even numbers
print('list_even_no:',even) #list containing even integers

odd = list(filter(lambda n : n%2 != 0,no))
print('list_odd_no:',odd) # list containing odd integers

## Map takes some value and it apply some operations to it
# Here we are doing cube on list of even no.
cubes =  list(map(lambda n : n**3,even))
print('Cubes:',cubes)

## If you want add,multiply or any other operations to a large chunk of data we use Reduce

sum = reduce(lambda a,b : a+b, cubes)
print('Sum of cubes:', sum)
## For understanding how lambda work with cubes a=8 b=512 then a=520 b=1728 .......

'''
output:
list_even_no: [2, 8, 12, 34, 36, 38]
list_odd_no: [3, 5, 7, 9, 11, 13, 23, 25]
Cubes: [8, 512, 1728, 39304, 46656, 54872]
Sum of cubes: 143080

'''