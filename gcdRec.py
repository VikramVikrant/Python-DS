##Recursive method to find gcd
def gcd(a,b):
    if a==0:      ##if any one of the no. is zero
        return b
    if b==0:
        return a
    if a==b:   ##base Case
        return a

    if a>b:
        return gcd(a-b,b)
    return gcd(a,b-a)

a = int(input("Enter first no:"))
b = int(input("Enter second no:"))
result = gcd(a,b)
print(f'Highest common factor of {a} and {b} is {result}.')