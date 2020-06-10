#https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    # write your code here
    a = line.split()
    n = '-'.join(a)
    return n

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
