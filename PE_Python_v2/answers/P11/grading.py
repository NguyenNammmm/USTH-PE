def weighted_mean(marks, credits):
    if not marks:
        return None
    return sum(m*c for m,c in zip(marks,credits)) / sum(credits)
