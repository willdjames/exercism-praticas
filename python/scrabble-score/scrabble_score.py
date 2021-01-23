
notas = [[['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 1],
         [['D', 'G'], 2],
         [['B', 'C', 'M', 'P'], 3],
         [['F', 'H', 'V', 'W', 'Y'], 4],
         [['K'], 5],
         [['J', 'X'], 8],
         [['Q', 'Z'], 10]]


def score(word):
    total = 0
    word = word.upper()
    for letra in word:
        for n in notas:
            if letra in n[0]:
                total += n[1]
    return total