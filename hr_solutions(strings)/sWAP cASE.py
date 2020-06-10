#https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    n = ''
    for letter in s:
        if letter==letter.lower():
            n+=letter.upper()
        else:
            n+=letter.lower()
    return n

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
