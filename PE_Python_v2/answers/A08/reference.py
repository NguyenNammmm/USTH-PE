# unix_spawn.py (POSIX)
import os,sys
def unix_spawn():
    pid=os.fork()
    if pid==0:
        try: os.execv(sys.executable,[sys.executable,"-c","print(123)"])
        except OSError: os._exit(127)
    _,status=os.waitpid(pid,0)
    return os.waitstatus_to_exitcode(status)
# windows_spawn.py (cũng có thể chạy cross-platform)
import subprocess
def windows_spawn():
    process=subprocess.Popen([sys.executable,"-c","print(123)"],shell=False)
    return process.wait(timeout=5)
