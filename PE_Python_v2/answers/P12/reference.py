def load_names(path):
    names = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            name = line.strip()
            if name:
                names.append(name)
    return names