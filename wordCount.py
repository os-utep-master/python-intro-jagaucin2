# imports
import sys
import re
import os


# arguments for input an output file
inFile = sys.argv[1]
outFile = sys.argv[2]

# open the input file
inputFile = open(inFile, 'r');

# empty list for words
wordList = []


for line in inputFile:
    # split by punctuation including spaces
    line = line.strip()
    word = re.split("[ \"\t.,;:'-]", line)

    # place into a list
    for key in word:
        # make all lowercase
        wordList.append(key.lower())

# sorted list
wordList.sort()

# remove ' ' elements that appeared on the list
while wordList.count(''):
    wordList.remove('')

# create dictionary
tempList = dict.fromkeys(wordList, 0)

# iterate over list and over dictionary and increase its count by 1 everytime it appears
for key in tempList:
    for word in wordList:
        if key == word:
            tempList[key] += 1

# write to file
outPut = open("myOutput.txt", "w+")
for key in tempList:
    outPut.write("%s %d\n" % (key, tempList.get(key)))

outPut.close()















