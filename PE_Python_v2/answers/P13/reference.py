def parse_score(text):
    try:
        score = float(text)
    except ValueError:
        return None
    if 0 <= score <= 10:
        return score
    return None