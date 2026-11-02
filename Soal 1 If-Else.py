# If: Do some code only IF some condition is TRUE
# Else: Do something else

# For example
age =int(input('Please enter your age: '))

if age >= 25:
    print('Anda Admin')
elif age >= 18:
    print('Anda Member')
elif age >= 14:
    print('Anda belum cukup umur :V')
else:
    print('Pergi kau SUKI!')