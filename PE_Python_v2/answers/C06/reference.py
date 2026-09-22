def labels(text):
    names=[line.strip().lower().title() for line in text.splitlines() if line.strip()]
    return [str(i).zfill(3)+": "+name for i,name in enumerate(names,1)]
def score_label(name,score):
    return "{}: {:.1f}".format(name,score)
