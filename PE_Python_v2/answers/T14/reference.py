import math
def score_valid(text):
    try: value=float(text)
    except ValueError: return False
    return math.isfinite(value) and 0<=value<=10
def make_validator(kind):
    if kind=="name": return lambda text: bool(text.strip())
    if kind=="score": return score_valid
    raise ValueError(kind)
