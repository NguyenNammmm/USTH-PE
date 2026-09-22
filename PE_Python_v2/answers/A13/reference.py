import socket
from urllib.request import urlopen
def tcp_line(host,port,message):
    with socket.create_connection((host,port),timeout=2) as sock:
        sock.sendall((message+"\n").encode("utf8"))
        with sock.makefile("rb") as stream: data=stream.readline(1025)
    if len(data)>1024 or not data.endswith(b"\n"): raise ValueError("framing")
    return data[:-1].decode("utf8")
def fetch_text(url):
    with urlopen(url,timeout=2) as response: data=response.read(4097)
    if len(data)>4096: raise ValueError("too large")
    return data.decode("utf8")
