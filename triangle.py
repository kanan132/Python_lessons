length = int(input('Enter number '))
symbol = input('Enter the symbol ')
width = 2 * length
for i in range(length):
   for n in range(width):
      print(end=' ')
   width -=1
   for n in range(i+1):
      print(symbol, end=' ')
   print(' ')
