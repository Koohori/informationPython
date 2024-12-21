import matplotlib.pyplot as plt
import numpy as np

f=open("worddic.txt", "r")
dicL=f.read().splitlines()





def occurance_histogram():
    new_list=[]
    occurance=[]
    letters=[u for u in range(1,(len(max(dicL,key=len))+1))]
    for i in dicL:
        x=len(i)
        new_list.append(x)
    for z in range(1,(len(max(dicL,key=len))+1)):
        # print(z)
        q=new_list.count(z)
        occurance.append(q)
    
    print(occurance)
    print(letters)
    plt.bar(letters,occurance)
    plt.show()


def anagrams():
    word=input('word to find anagram: ')
    length_word = len(word)
    for i in dicL:
            if len(i)==length_word and sorted(list(word))==sorted(list(i)) and i!=word:
                print(f'Anagram pair: {i} and {word}')

# occurance_histogram()
anagrams()