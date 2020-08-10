from functools import reduce
numbers = []
for i in range(1,101):
    numbers.append(i)
print(numbers)

## Now using reduce to sum the elements in the list
sum = reduce(lambda a,b: a+b,numbers)
print('Sum of 100 numbers:',sum)