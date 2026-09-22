from pathlib import Path
import json,zipfile,gzip,pickle
KEYS=("students","courses","marks")
def save_text_bundle(folder,state):
    folder=Path(folder); folder.mkdir(parents=True,exist_ok=True)
    for key in KEYS: (folder/(key+".txt")).write_text(json.dumps(state[key],ensure_ascii=False),encoding="utf8")
    with zipfile.ZipFile(folder/"students.dat","w",zipfile.ZIP_DEFLATED) as archive:
        for key in KEYS: archive.write(folder/(key+".txt"),arcname=key+".txt")
def load_text_bundle(folder):
    path=Path(folder)/"students.dat"
    if not path.exists(): return {key:{} for key in KEYS}
    with zipfile.ZipFile(path) as archive:
        return {key:json.loads(archive.read(key+".txt").decode("utf8")) for key in KEYS}
def save_pickle(path,registry):
    with gzip.open(path,"wb") as stream: pickle.dump(registry,stream,pickle.HIGHEST_PROTOCOL)
def load_pickle(path):
    if not Path(path).exists(): return None
    with gzip.open(path,"rb") as stream: return pickle.load(stream)
