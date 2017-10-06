import numpy as np
import matplotlib.pyplot as plt

f = open("file.txt", "r");

WordDictSet = set()
WordDict = {}

for line in f :
    words = line.split()
    index = 0
    for word in words :
#        if WordDict.has_key(word) :
#            continue
#        else :
             WordDictSet.add(word)
#             print("x: {0}".format(word))

numberWords = len(WordDictSet)

print("Number of words: ", numberWords)

#sort the dict in order
index = 0
for word in WordDictSet :
    WordDict[word] = index
    index = index + 1

InvertWordDict = {}

for word in WordDictSet :
    InvertWordDict[WordDict[word]] = word

x = np.zeros((numberWords, numberWords), dtype=np.int16)

f.close()
f = open("file.txt", "r");

prev_word = ""
for line in f :
    words = line.split()
    prev_word = ""

    for word in words :
        if prev_word == "" :
            pass     
        else:
            x[WordDict[prev_word], WordDict[word]] += 1
            x[WordDict[word], WordDict[prev_word]] += 1
        prev_word = word
print(x) 

U, s, Vh = np.linalg.svd(x, full_matrices = False);

plt.xlim([-1, 1])
plt.ylim([-1, 1])

for i in range(len(WordDict)) :
    print("[{0:.2f}, {1:.2f}]{2}".format(U[i,0], U[i,1], InvertWordDict[i]))
    plt.text(U[i, 1], U[i, 2], InvertWordDict[i])
plt.show()

'''
words = ["I", "like", "deep", "enjoy", "deep", "learning", "NLP", "flying"]

x = np.array([[0, 2, 1, 0, 0, 0, 0, 0],
              [2, 0, 0, 1, 0, 1, 0, 0],
              [1, 0, 0, 0, 0, 0, 1, 0],
              [0, 1, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 1],
              [0, 1, 0, 0, 0, 0, 0, 1],
              [0, 0, 1, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 1, 1, 1, 0]])

U, s, Vh = np.linalg.svd(x, full_matrices = False);

print(U)

plt.xlim([-1, 1])
plt.ylim([-1, 1])

for i in range(len(words)) :
    print("[{0:.2f}, {1:.2f}]{2}".format(U[i,0], U[i,1], words[i]))
    plt.text(U[i, 1], U[i, 2], words[i])
plt.show()
'''
        