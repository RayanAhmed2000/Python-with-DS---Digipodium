# This file is for defining functions which can be used in other pyhton files and notebooks

def char_counter(sentence):
    data={}
    for char in set(sentence):                  # convert sentence to set to keep only unique values
        print(char,sentence.count(char))
        data[char] = sentence.count(char)
    return data


def word_counter(sentence):
    data = {}
    words = sentence.split()
    for word in set(words):
        data[word] = words.count(word)
    return data

def remove_punc(sentence):
    '''removes punctuation (TBC)'''
    pass