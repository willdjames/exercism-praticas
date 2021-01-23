def latest(scores):
    return personal_top_three(scores)[-1]


def personal_best(scores):
    return personal_top_three(scores)[0]


def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[0:3]
