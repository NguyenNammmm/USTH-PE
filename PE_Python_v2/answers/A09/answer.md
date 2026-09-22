# A09 - Luồng chuẩn, pipe và vòng đời process

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import subprocess
def run_child(args,text,timeout):
    process=subprocess.Popen(args,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,shell=False)
    timed_out=False
    try:
        out,err=process.communicate(text,timeout=timeout)
    except subprocess.TimeoutExpired:
        timed_out=True; process.kill(); out,err=process.communicate()
    return dict(stdout=out,stderr=err,returncode=process.returncode,timed_out=timed_out)
```

## Đáp án kiểm tra hiểu

1. Sau TimeoutExpired, process đã chắc bị dừng chưa?

Đáp án: Chưa với Popen.communicate

- Chưa với Popen.communicate: Đúng: caller phải xử lý vòng đời.
- Luôn tự dừng: Không được giả định vậy.
- Luôn exit0: Timeout không là thành công.

