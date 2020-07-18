full_name=lambda first,last:f'Name:{first.title()} {last.title()}'
occupation=lambda occ:f'Occupation:{occ}'
Age=lambda age:f'Age:{age}'

print(full_name('APJ','abdul kalam'))
print(occupation('Retired President'))
print(Age(45))