from threading import Thread,Lock
def count_parallel(workers,iterations):
    count=0; lock=Lock()
    def work():
        nonlocal count
        for _ in range(iterations):
            with lock: count+=1
    threads=[Thread(target=work) for _ in range(workers)]
    for thread in threads: thread.start()
    for thread in threads: thread.join()
    return count
