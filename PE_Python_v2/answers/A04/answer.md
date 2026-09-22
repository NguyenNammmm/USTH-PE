# A04 - Nén bytes và đóng gói nhiều file

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
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
```

## Đáp án kiểm tra hiểu

1. Nén chuỗi ngắn xong file lớn hơn có chứng minh thuật toán hỏng không?

Đáp án: Không, còn header và overhead

- Có: Không được kết luận chỉ theo kích thước.
- Không, còn header và overhead: Đúng: kiểm tra round-trip là tiêu chí chính.
- Chỉ đúng khi file rỗng: Cả chuỗi ngắn không rỗng cũng có thể lớn hơn.

