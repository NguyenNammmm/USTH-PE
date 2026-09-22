def summarize(marks,remove_id):
    remaining=marks.copy()
    removed=remaining.pop(remove_id,None)
    best=min(remaining,key=lambda k:(-remaining[k],k)) if remaining else None
    worst=min(remaining,key=lambda k:(remaining[k],k)) if remaining else None
    return dict(remaining=remaining,removed=removed,best=best,worst=worst)
