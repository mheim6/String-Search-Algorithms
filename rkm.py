####################################
#
# Monica Heim
# Driver Code
# Automata Algorithms and Complexity
# Assignment 3
####################################

def mapout():
    words={}
    for i in range(0, 26):
        key = chr(i + 97)
        words[key] = ord(key) - 96
    return words

hashDict = mapout()

def indexValue(text):
    value = 0
    exponent = len(text) - 1
    for i in range(0, len(text)):
        x = hashDict[text[i]] * 10**exponent
        value = value + x
        exponent = exponent - 1
    return value


def rabin_karp(word, text):
    matchValue = indexValue(text)
    if text == "" or word == "":
        return None
    if len(word) < len(text):
        return None
    indexArr = []
    hashing = indexValue(word[0:len(text)])
    for i in range(0, len(word)):
        if matchValue == hashing:
            if text == word[i:i + len(text)]:
                indexArr.append(i)
        hashing = hashing - (indexValue(word[i:i + 1])
                                                * 10**(len(text) - 1))
        hashing = hashing * 10
        hashing = hashing + indexValue(word[i + len(text):
                                                i + len(text) + 1])
    if not indexArr:
        print("The text currenty not found:")
        indexArr.append(-1)
        return indexArr
    else:
        print("The text is currently found at :")
        return indexArr
