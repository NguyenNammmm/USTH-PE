def advance(x,v,dt,limit):
    if limit<=0 or dt<0: raise ValueError("bounds")
    if v==0: return x,0
    phase=(x+v*dt)%(2*limit)
    if phase==0: return 0,abs(v)
    if phase==limit: return limit,-abs(v)
    return (phase,v) if phase<limit else (2*limit-phase,-v)
