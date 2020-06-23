'''sudo apt-get install python3-tk   to get image of word cloud
pip install vocabulary
pip install wordcloud'''

import requests
from vocabulary.vocabulary import Vocabulary as vb
import wordcloud
from matplotlib import pyplot as plt
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "in", "on", "not", "for" \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", "for", "we",\
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", "project", "gutenberg", "ebook"]
url = input('Please enter url: ')
response = requests.get(url)
def most_frequency_words(string):
    d = {}
    string = string.strip()
    a = string.split()
    for word in a:
        w = word.lower()
        if w not in uninteresting_words and w.isalpha():
            if w not in d:
                d[w] = 1
            else:
                d[w] +=1
    return d

def antonyms(dict):
    list_of_words,a = [], []
    antonyms = {}
    for value in dict.values():
        list_of_words.append(value)
    
    list_of_words.sort()
    for i in range(-1, -30, -1):
        for key in dict.keys():
            if dict[key] == list_of_words[i]:
                a.append(key)
    for elem in a:
        if vb.antonym(elem) != False:
            antonyms[elem] = []
            antonyms[elem].append(vb.antonym(elem, format='list'))

    for k, v in antonyms.items():
        print(f'Antonym for {k.upper()} is {v} ')


def word_cloud(dict):
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(dict)
    return cloud.to_array()

#print(most_frequency_words(response.text))
#antonyms(most_frequency_words(response.text))

myimage = word_cloud(most_frequency_words(response.text))
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
