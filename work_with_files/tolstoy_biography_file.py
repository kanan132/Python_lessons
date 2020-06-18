'''Script works with tolstoy.txt file'''

big_string = ''
with open('tolstoy.txt', 'r') as inf:
    for line in inf:
        line = line.strip()
        big_string+=line
vowels = ['e', 'u', 'i', 'o', 'a', ]
def count_vowels(string):
    counter = 0
    for letter in big_string:
        a = letter.lower()
        if a in vowels:
            counter +=1
    return counter

print(f'Number of symbols is {len(big_string)} and number of vowels is {count_vowels(big_string)}')


