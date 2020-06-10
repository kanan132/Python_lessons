#https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    counter=0
    length = len(sub_string)
    for i in range(len(string)-length+1):
        if sub_string==string[i:length+i]:
            counter+=1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
