from collections import deque
def schedule(jobs,policy,quantum=2):
    if policy not in ("fcfs","sjf","priority","rr") or quantum<=0:
        raise ValueError("policy/quantum")
    ordered=list(jobs)
    if policy=="sjf": ordered.sort(key=lambda row:row[1])
    if policy=="priority": ordered.sort(key=lambda row:row[2])
    queue=deque((sid,burst) for sid,burst,_ in ordered)
    time=0; trace=[]
    while queue:
        sid,remaining=queue.popleft()
        duration=min(quantum,remaining) if policy=="rr" else remaining
        trace.append((sid,time,time+duration)); time+=duration
        if remaining>duration: queue.append((sid,remaining-duration))
    return trace
