length = int(input('Enter number: '))
symbol = input('Enter the symbol: ')

def print_triangle(length, symbol):
   for i in range(length):
      print(end=' '*(length-i))
      for j in range(i+1):
         print(symbol, end=' ')
      print(' ')
   
   
   
print_triangle(length, symbol)
