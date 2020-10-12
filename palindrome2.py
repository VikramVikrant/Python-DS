## To check whether a string is palindrome or not.
x=input()
w=''
for i in x:   ## if we take input string as mada
    w = i + w ## see here i + w ,so it's added like this m,am,dam,adam
    if(x==w):
        print('Yes it is a palindrome.')

if(x!=w):
    print("It's not a palindrome.")