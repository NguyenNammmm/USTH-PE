import subprocess
def run_child(args,text,timeout):
    process=subprocess.Popen(args,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,shell=False)
    timed_out=False
    try:
        out,err=process.communicate(text,timeout=timeout)
    except subprocess.TimeoutExpired:
        timed_out=True; process.kill(); out,err=process.communicate()
    return dict(stdout=out,stderr=err,returncode=process.returncode,timed_out=timed_out)
