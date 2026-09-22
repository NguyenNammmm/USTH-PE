def select_parts(text,items):
    return text[:3],text[::-1],items[-3:],items[1::2]
def replace_middle(items):
    result=items.copy()
    result[1:3]=[99]
    return result
