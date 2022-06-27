import pandas as pd
import numpy as np
import itertools
import math


#this function filter the list and remove element on the basis of input it takes one letter input only
def letter(x,y,z,lst):
    if(y=='g'):
        return list(filter(lambda word: x  in word[z],lst))
    elif(  y=='y'):
        return list(filter(lambda word: x in word and x not in word[z],lst))
    elif(y=='x'):
        return list(filter(lambda word: x not in word,lst))


#this function take word as the input return all possible answer list
def words(x, y, lst):
    lst = letter(x[0], y[0], 0, lst)
    lst = letter(x[1], y[1], 1, lst)
    lst = letter(x[2], y[2], 2, lst)
    lst = letter(x[3], y[3], 3, lst)
    return letter(x[4], y[4], 4, lst)


#this function recursivley store all pattern of x,y,g of lenght 5
def printAllKLength(set, k):
	n = len(set)
	printAllKLengthRec(set, "", n, k)

def printAllKLengthRec(set, prefix, n, k):
	if (k == 0) :
		lst1.append(prefix)
		return
	for i in range(n):
		newPrefix = prefix + set[i]
		printAllKLengthRec(set, newPrefix, n, k - 1)


#list 1 will contain all permutation of x,y,g of length 5
lst1=[]
set1 = ['x', 'y','g']
k = 5
printAllKLength(set1, k)


#lst2 contain the number of possiblity after a each input and this function returns score of each word based on the list of possiblity
#this function calculate the score of one word present in the list based on information theory
def expexted_score_of_word(word,lst):
    lst2=[]
    for i in range(len(lst1)):
        lst2.append(len(words(word,lst1[i],lst)))
    s=0
    for i in range(len(lst2)):
        if(lst2[i]!=0):
            s = s + ((lst2[i])*(-math.log(lst2[i]/len(lst),2))/len(lst))
    return s


#lst 3 contain all the socres of word
#when ran iterativley all words in list got a score
def lst_of_words_and_scores(lst):
    lst3=[]
    for i in range(len(lst)):
        lst3.append(expexted_score_of_word(lst[i],lst))
    return lst3



#now our list contain list of all 5 letter words
lst=[]
fhand = open('words_len5.txt')
for line in fhand:
    lst.append(line.strip())
fhand.close()




print("in result print\nx for grey \ny for yellow \ng for green")
a=1
result=''
print("top three guess you can make are")
print("tares")
print("lares")
print("arise")
print("teras")
print("rales")
while 1:
    word_written = input("\nenter your word ")
    result = input("result you got ")
    if result=='ggggg' : break
    lst = words(word_written, result, lst)
    a+=1
    res = dict(zip(lst, lst_of_words_and_scores(lst)))
    my_keys = sorted(res, key=res.get, reverse=True)[:5]
    print("some of top guesses you can make are")
    if len(my_keys)<=2:
        print(my_keys[0])
    elif len(my_keys)<=4:
        print(my_keys[0])
        print(my_keys[1])
        print(my_keys[2])
    else :
        print(my_keys[0])
        print(my_keys[1])
        print(my_keys[2])
        print(my_keys[3])
        print(my_keys[4])


print("\nyou got you result in",a,"iteration")