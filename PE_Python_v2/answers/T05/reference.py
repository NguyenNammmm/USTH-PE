from pathlib import Path
import shutil
from tkinter import filedialog,messagebox
def copy_file(source,destination_dir):
    target=Path(destination_dir)/Path(source).name
    shutil.copy2(source,target)
    return str(target)
def choose_and_copy(root):
    source=filedialog.askopenfilename(parent=root)
    if not source: return None
    folder=filedialog.askdirectory(parent=root)
    if not folder: return None
    try:
        result=copy_file(source,folder)
    except OSError as error:
        messagebox.showerror("Khong sao chep",str(error),parent=root)
        return None
    messagebox.showinfo("Da sao chep",result,parent=root)
    return result
