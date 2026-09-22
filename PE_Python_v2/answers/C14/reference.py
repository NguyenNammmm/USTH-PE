from collections import Counter
def report(ids,scores):
    if len(ids)!=len(scores):
        raise ValueError("length mismatch")
    pairs=[(sid,score) for sid,score in zip(ids,scores) if score>=5]
    return [(i,sid,score) for i,(sid,score) in enumerate(pairs,1)]
def top_votes(ids,k):
    return Counter(ids).most_common(k)
