import re

def abbreviate(words):
    words = re.sub(r"'", 'x', words) # trata apostofre
    words = words.title()
    res = re.findall(r"[A-Z]+", words)
    return ''.join(res)
