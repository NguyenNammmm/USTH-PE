import re
def parse_filename(filename):
    if not filename.endswith(".txt"):
        raise ValueError("extension")
    parts=filename.removesuffix(".txt").split("-")
    if len(parts)!=4:
        raise ValueError("fields")
    name,age_text,distance,stroke=parts
    if not name or not stroke or not age_text.isdecimal():
        raise ValueError("metadata")
    if not re.fullmatch(r"[1-9]\d*m",distance):
        raise ValueError("distance")
    return dict(name=name,age=int(age_text),distance=distance,stroke=stroke)
