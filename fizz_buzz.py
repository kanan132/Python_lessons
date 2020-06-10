fizz_buzz_list=[]
for i in range(1, 101):
    if i%3==0:
        if i%5==0:
            fizz_buzz_list.append('FizzBuzz')
        else:
            fizz_buzz_list.append('Fizz')
    elif i%5==0:
        fizz_buzz_list.append('Buzz')
    else:
        fizz_buzz_list.append('Nothing')

print('Fizz: {}, Buzz: {}, FizzBuzz: {}, Nothing: {}'.format(fizz_buzz_list.count('Fizz'), fizz_buzz_list.count('Buzz'),fizz_buzz_list.count('FizzBuzz'),fizz_buzz_list.count('Nothing')))
