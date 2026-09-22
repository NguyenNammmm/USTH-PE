import copy,gzip,pickle,os,uuid
from pathlib import Path
from threading import Thread
from queue import Queue
def start_save(state,path):
    snapshot=copy.deepcopy(state); path=Path(path); results=Queue()
    def work():
        temporary=path.with_name(path.name+"."+uuid.uuid4().hex+".tmp")
        try:
            with gzip.open(temporary,"wb") as stream: pickle.dump(snapshot,stream,pickle.HIGHEST_PROTOCOL)
            os.replace(temporary,path); results.put(("ok",str(path)))
        except Exception as error: results.put(("error",str(error)))
        finally:
            if temporary.exists(): temporary.unlink()
    worker=Thread(target=work); worker.start(); return worker,results
