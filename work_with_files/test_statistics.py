chapter = ''
with open('robinson_chapter1.txt', 'r') as inf:
    for line in inf:
        line = line.strip()
        chapter+=line
def most_frequent_letter(string):
    d_letters = {}
    for letter in string:
        ll = letter.lower()
        if ll.isalpha():
            if ll not in d_letters:
                d_letters[ll] = 1
            else:
                d_letters[ll] +=1
    max_letter, v = 0, 0
    for key, value in d_letters.items():
        if value>max_letter:
            max_letter = value
            v = key

    return f'The most frequency letter is {v.upper()} : {max_letter}'

print(most_frequent_letter(chapter))

def count_letters(string):
    counter = 0
    for letter in string:
        if letter.isalpha():
            counter+=1
    return f'Number of letters is {counter}'


print(count_letters(chapter))


def count_words(string):
    counter = 0
    list_of_words = string.split()
    for word in list_of_words:
        if word.isalpha():
            counter +=1

    return f'Number of words is {counter}'

print(count_words(chapter))

def most_frequent_word(string):
    d_words = {}
    list_of_words = string.split()
    for word in list_of_words:
        w = word.lower()
        if w.isalpha():
            if w not in d_words:
                d_words[w] = 1
            else:
                d_words[w]+=1
    max_word, v = 0, 0
    for key, value in d_words.items():
        if value>max_word:
            max_word = value
            v = key

    return f'The most frequency word is {v.upper()} : {max_word}'


print(most_frequent_word(chapter))







