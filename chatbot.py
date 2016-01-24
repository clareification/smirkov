import re
import pickle
import string
import random
def findNext (curr, pairdict, worddict):
    if curr in worddict:
        print curr + "\n"
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


pairfile= "pairs.pkl"
wordfile = "words.pkl"
wfile = open(wordfile, 'rb')
pfile = open(pairfile, 'rb')
tuple_data = pickle.load(pfile)
word_data = pickle.load(wfile)
seed = "boat"
print type (word_data)
if seed in word_data:
    print 'yes'
else:
    print 'not in list'
phrase = ""
for i in range(10):
    phrase += " " + seed
    seed = findNext(seed, tuple_data, word_data)
print phrase
