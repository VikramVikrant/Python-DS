numbers='one','two','three','four'
print(type(numbers))
func=[]
for n in numbers:
    func.append(lambda n=n: print(n))

for f in func:
    print(f)
    f()

'''
<class 'tuple'>
<function <lambda> at 0x03B5B340>
one
<function <lambda> at 0x03B5B2F8>
two
<function <lambda> at 0x03B5B388>
three
<function <lambda> at 0x03B5B3D0>
four

'''