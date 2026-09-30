import threading
from inheritance_intermediate import C as BaseC


class C(BaseC):
    def _compile_worker(self, n):
        message = f"Compiling C code using {n} threads"
        message += f" with standard version {self.std_version}"
        print(message)

    def parallel_compile(self, n):
        if type(n) is not int or n <= 0:
            raise ValueError("n must be a positive integer")

        threads = []
        for index in range(n):
            worker = threading.Thread(target=self._compile_worker, args=(n,))
            threads.append(worker)

        for worker in threads:
            worker.start()

        for worker in threads:
            worker.join()
