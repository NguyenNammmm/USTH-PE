TRANSITIONS={("new","admit"):"ready",("ready","dispatch"):"running",
             ("running","io"):"waiting",("waiting","complete"):"ready",
             ("running","preempt"):"ready",("running","exit"):"terminated"}
def next_state(state,event):
    try: return TRANSITIONS[state,event]
    except KeyError: raise ValueError("invalid transition") from None
