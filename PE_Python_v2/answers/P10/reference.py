def mean_score(scores):
    if not scores:
        return None
    return sum(scores) / len(scores)