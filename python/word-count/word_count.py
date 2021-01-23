from collections import Counter
import re

def count_words(sentence):
    sentence = sentence.replace(',', ' ').replace('_', ' ').lower().split()
    
    return dict(Counter([re.search(r"\w+'t|\w+", x).group()
                        for x in sentence]))
