for i in range(1, 101):
    if i%3==0:
        if i%5==0:
            print('{}: FizzBuzz'.format(i))
        else:
            print('{}: Fizz'.format(i))
    elif i%5==0:
        print('{}: Buzz'.format(i))
    else:
        print('{}: Nothing'.format(i))
