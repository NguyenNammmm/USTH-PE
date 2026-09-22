from threading import Thread
from queue import Queue

def run_job(values):
    q = Queue()
    def work():
        q.put([value * value for value in values])
    thread = Thread(target=work)
    thread.start()
    thread.join()
    return q.get()