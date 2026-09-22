import gzip,bz2,zlib,io,zipfile
CODECS={"gzip":gzip,"bz2":bz2,"zlib":zlib}
def codec(method):
    if method not in CODECS: raise ValueError("method")
    return CODECS[method]
def compress_bytes(data,method): return codec(method).compress(data)
def decompress_bytes(blob,method): return codec(method).decompress(blob)
def pack_files(files):
    buffer=io.BytesIO()
    with zipfile.ZipFile(buffer,"w",compression=zipfile.ZIP_DEFLATED) as archive:
        for name,data in files.items():
            if "/" in name or "\\" in name or name in (".",".."): raise ValueError("basename")
            archive.writestr(name,data)
    return buffer.getvalue()
def unpack_files(blob):
    with zipfile.ZipFile(io.BytesIO(blob)) as archive:
        return {name:archive.read(name) for name in archive.namelist()}
