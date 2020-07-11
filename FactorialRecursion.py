#python ds recursion q1
def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))

num=int(input("Enter the no. whose factorial you want:"))
print(f"The factorial of {num} is {factorial(num)}")