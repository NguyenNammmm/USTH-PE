def edit(values,extras,target):
    result=values.copy()
    result.extend(extras)
    if target in result:
        result.remove(target)
    removed=result.pop() if result else None
    result.reverse()
    return result,removed
