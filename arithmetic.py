'''Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
The sum of a and b
The difference when b is subtracted from a
The product of a and b
The quotient when a is divided by b
The remainder when a is divided by b
The result of a of power b'''

a = int(input('Please enter the first integer: '))
b = int(input('Please enter the second integer: '))
print('The sum is {}'.format(a+b))
print('The difference is {}'.format(b-a))
print('The product is {}'.format(a*b))
print('The quotient is {}'. format(a//b))
print('The remainder is {}'.format(a%b))
print('The power is {}'.format(a**b))
