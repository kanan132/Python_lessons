'''Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre.'''


length = int(input('Enter length of area: '))
width = int(input('Enter width of area: '))
square_feet = 43.560
square = length*width/square_feet
print('The square of area is {:.2f} in acres'.format(square))
