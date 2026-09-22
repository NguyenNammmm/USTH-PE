def append_line(path,text):
    with open(path,"a",encoding="utf8") as stream:
        stream.write(text+"\n")
        stream.flush()
def read_status(path):
    try:
        with open(path,encoding="utf8") as stream:
            return "ok",stream.read()
    except FileNotFoundError:
        return "missing",None
    except PermissionError:
        return "denied",None
