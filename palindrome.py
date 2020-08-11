def palindrome(str):
    if str == str[::-1]:
        print('It is a palindrome.')
    else:
        print('It is not a palindrome.')

palindrome('madam')
palindrome('hello')
palindrome('121')
palindrome('malayalam')

