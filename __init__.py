from itertools import permutations
from nltk.corpus import words
def valid_word(list_of_words,list_of_sizes):
    if type(list_of_sizes) == int :
        list_of_sizes = list(list_of_sizes)
    list_of_english_words=[]
    for i in list_of_sizes:
        possible_permutations=list(permutations(list_of_words,i))
        for j in possible_permutations:
            k="".join(p for p in j)
            if k in words.words():
                if k not in list_of_english_words:
                    list_of_english_words.append(k)
    return list_of_english_words
                

