from threading import Thread,Event
from queue import Queue
class SquareWorker(Thread):
    def __init__(self,job_id,value,output,stop_event):
        super().__init__(); self.job_id=job_id; self.value=value; self.output=output; self.stop_event=stop_event
    def run(self):
        if not self.stop_event.is_set(): self.output.put((self.job_id,self.value**2))
def run_many(values):
    output=Queue(); stop=Event()
    workers=[SquareWorker(i,value,output,stop) for i,value in enumerate(values)]
    for worker in workers: worker.start()
    for worker in workers: worker.join()
    result={}
    while not output.empty():
        i,value=output.get(); result[i]=value
    return [result[i] for i in range(len(values))]
