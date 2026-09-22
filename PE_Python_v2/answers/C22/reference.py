import os
from pathlib import Path
def text_files(root):
    root=Path(root)
    result=[]
    for folder,dirs,files in os.walk(root,followlinks=False):
        for name in files:
            if name.endswith(".txt"):
                result.append((Path(folder)/name).relative_to(root).as_posix())
    return sorted(result)
