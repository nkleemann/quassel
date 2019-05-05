#   Generate random names, words, or text similar to the 
#   ones you provide in "sample.txt".
#
# 
#   Usage:
#       python3 generate.py <howManyNames> <infixLength>
#
#   
#   Comments in this file refer to NAMES but you can 
#   generate anything you want, it just depends on your 
#   input data and treshold values.
#
#   This is nothing fancy, just a random pick from anarrowed 
#   down set of pre-, in- and suffixes chosen and filtered by 
#   number of occurence in the sample data.
#

import random
from sys import argv
from collections import Counter

#
#       GLOBALS
# 

# How many names we generate
randNameCount = int(argv[1])
# How long should those names be
infixLength   = int(argv[2])

# Filter out characters with occurences below those thresholds
prefixOccurenceThreshold = 2
infixOccurenceThreshold  = 4
suffixOccurenceThreshold = 2

#
#       UTILS
#

# Filter characters with occurences below threshold
def filterOccurences(counter, treshold):
    return {x : counter[x] for x in counter if counter[x] >= treshold}

# Convert Counter object back to a list with multiple occurences
# We need those doubled elements to skew the chance of getting
# a char that has a high representation
def counterToList(counter):
    l = []
    for elem, occ in counter.items():
        for i in range(0, occ):
            l.append(elem)
    return l


def pickPrefixFrom(l):
    return random.choice(l)


def pickInfixFrom(l, howMany):
    infix = ""
    
    for i in range(0, howMany):
        infix += random.choice(l)
    
    return infix


def pickSuffixFrom(l):
    return random.choice(l)


#
#       EXTRACT & PREPARE NAMES FROM FILE
#

namesList = open("sample.txt", "r").read().split("\n")

prefixes  = []
infixes   = []
sufffixes = []

for name in namesList:
    prefixes.append(name[0])
    sufffixes.append(name[-1])
    for c in name[1:-1]:
        infixes.append(c.lower())


#
#       ANALYZE OCCURENCES & GENERATE NAMES
#

prefixesFiltered = counterToList(filterOccurences(Counter(prefixes),  prefixOccurenceThreshold))
infixesFiltered  = counterToList(filterOccurences(Counter(infixes),   infixOccurenceThreshold))
suffixesFiltered = counterToList(filterOccurences(Counter(sufffixes), suffixOccurenceThreshold))


for i in range(0, randNameCount):
    randName = pickPrefixFrom(prefixesFiltered) + pickInfixFrom(infixesFiltered, infixLength) + pickSuffixFrom(suffixesFiltered)
    print(randName)
