def swim_report(line):
    if not line.strip():
        return {"count": 0, "mean": None}
    values = []
    for part in line.split(","):
        minutes, rest = part.strip().split(":")
        seconds, hundredths = rest.split(".")
        values.append(int(minutes)*6000 + int(seconds)*100 + int(hundredths))
    n = len(values)
    average = (2*sum(values) + n) // (2*n)
    minutes, remainder = divmod(average, 6000)
    seconds, hundredths = divmod(remainder, 100)
    return {"count": n, "mean": f"{minutes}:{seconds:02d}.{hundredths:02d}"}