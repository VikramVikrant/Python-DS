##Using Decorators we can extra features in an existing function

def div(a,b):
    print(a/b)

def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div = smart_div(div)

div(2,4)
div(6,8)

'''
output:
2.0
1.3333333333333333

'''