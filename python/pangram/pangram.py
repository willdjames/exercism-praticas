import re

def is_pangram(sentence):
    sentence = sentence.lower()
    letters = []
    for s in sentence:
        if re.match('[a-z]', s):
            letters.append(s)
    
    return len(set(letters)) == 26
