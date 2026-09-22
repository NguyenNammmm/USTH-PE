def collect(start,stop,step,blocked):
    result=[]
    for n in range(start,stop,step):
        if n==blocked:
            break
        if n%3==0:
            continue
        result.append(n)
    return result
