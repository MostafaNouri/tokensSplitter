import re
import os

def getMaxLength(sentence, list):
    maxLength = 0
    if len(sentence) > max(list.keys()):
        maxLength = max(list.keys())
    else:
        maxLength = len(sentence)

    return maxLength

def tokensSplitter(sentence, list):
    maxLength = getMaxLength(sentence, list)
    s = ""

    while sentence:
        if sentence[:maxLength] in list.get(maxLength, ''):
            s += sentence[:maxLength] + " "
            sentence = sentence.replace(sentence[:maxLength], '')
            maxLength = getMaxLength(sentence, list)
        else:
            maxLength -= 1
            if maxLength == 0:
                s = "Error"
                break

    return s

if not os.path.exists('output'):
    os.makedirs('output')

# English version
enTokens = open("en.tokens.en","r", encoding="utf8")
enMergedTokens = open("mergedTokens.en","r", encoding="utf8")
enOutput = open("output/enSentences.txt", "w+", encoding="utf8")

enList = dict()

enTokensArray = enTokens.read().splitlines()
enMergedTokensArray = enMergedTokens.read().splitlines()

for word in enTokensArray:
    if len(word) in enList:
        enList[len(word)].append(word)
    else:
        enList[len(word)] = [word]

counter = 1
for sentence in enMergedTokensArray:
    enOutput.write("%s) %s -> %s\n" % (str(counter), sentence, tokensSplitter(sentence, enList)))
    counter += 1

print("English sentences processing finished!")
enOutput.close()
enTokens.close()
enMergedTokens.close()

# Persian version
faTokens = open("fa.words.txt", "r", encoding="utf8")
faMergedTokens = open("mergedTokens.fa", "r", encoding="utf8")
faOutput = open("output/faSentences.txt", "w+", encoding="utf8")

faTokensArray = []

faList = dict()

for line in faTokens:
    word = re.sub(r"[0-9]|\t|\n|\s", "", line)
    if len(word) in faList:
        faList[len(word)].append(word)
    else:
        faList[len(word)] = [word]

faMergedTokensArray = faMergedTokens.read().splitlines()

counter = 1
for sentence in faMergedTokensArray:
    faOutput.write("%s) %s -> %s\n" % (str(counter), sentence + u'\u202B', tokensSplitter(sentence, faList) + u'\u202B'))
    counter += 1

print("Persian sentences processing finished!")
faOutput.close()
faTokens.close()
faMergedTokens.close()

print("\ngo to output folder and see outputs.")