import re
import pickle
import string
import random

#Generate next word given a seed word
def findNext (curr, pairdict, worddict):
    if curr in worddict:
        wBest = curr
        pBest = 0
        candidates = []
        for pair in pairdict.keys():
            if pair[0] == curr:
                candidates.append(pair[1])
                # if pairdict[pair]>pBest:
                #     wBest = pair[1]
                #     pBest = pairdict[pair]

        return candidates[random.randint(0, len(candidates) -1)]
    else:
        print "not found"

#load data -- you might need to generate this first with parser.py
pairfile= "pairs.pkl"
wordfile = "words.pkl"
linefile = "lines.pkl"
wfile = open(wordfile, 'rb')
pfile = open(pairfile, 'rb')
lfile = open(linefile, 'rb')
lines = pickle.load(lfile)
tuple_data = pickle.load(pfile)
word_data = pickle.load(wfile)
for j in range (0, 10):
    lineSeed = random.randint(0, len(lines)-1)
    print lines[lineSeed]
    print "hello"
seedIndex = random.randint(0, len(word_data) -1)
seed = word_data[seedIndex]
phrase = ""
for i in range(10):
    phrase += " " + seed
    seed = findNext(seed, tuple_data, word_data)
print phrase
