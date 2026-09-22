import numpy as np
def gpa(marks,credits):
    m=np.asarray(marks,dtype=float); c=np.asarray(credits,dtype=float)
    if m.ndim!=1 or c.ndim!=1 or m.shape!=c.shape:
        raise ValueError("shape")
    if not (np.isfinite(m).all() and np.isfinite(c).all()) or (m<0).any() or (m>10).any() or (c<=0).any():
        raise ValueError("values")
    return float(np.dot(m,c)/c.sum()) if len(m) else None
def ranking(records):
    rows=[(sid,gpa(*pair)) for sid,pair in records.items()]
    return sorted(rows,key=lambda row:(row[1] is None,-row[1] if row[1] is not None else 0,row[0]))
