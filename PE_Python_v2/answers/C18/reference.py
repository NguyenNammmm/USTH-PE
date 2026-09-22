from pathlib import Path
from statistics import mean
from decimal import Decimal,ROUND_HALF_UP
from metadata import parse_filename
def file_report(path):
    result=parse_filename(Path(path).name)
    with open(path,encoding="utf8") as stream:
        lines=stream.readlines()
    line=lines[0].strip() if lines else ""
    values=[]
    if line:
        for token in line.split(","):
            minute,rest=token.strip().split(":")
            second,hundredth=rest.split(".")
            values.append(int(minute)*6000+int(second)*100+int(hundredth))
    formatted=None
    if values:
        rounded=int(Decimal(str(mean(values))).quantize(Decimal("1"),rounding=ROUND_HALF_UP))
        minute,rest=divmod(rounded,6000)
        second,hundredth=divmod(rest,100)
        formatted=f"{minute}:{second:02d}.{hundredth:02d}"
    return dict(result,count=len(values),mean=formatted)
