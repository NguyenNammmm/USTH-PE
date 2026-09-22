import shlex,subprocess,time,contextlib
def parse(line):
    lexer=shlex.shlex(line,posix=True,punctuation_chars="|<>"); lexer.whitespace_split=True; lexer.commenters=""
    tokens=list(lexer); stages=[[]]; source=target=None; i=0
    while i<len(tokens):
        token=tokens[i]
        if token=="|":
            if not stages[-1] or target is not None: raise ValueError("pipe")
            stages.append([])
        elif token in ("<",">"):
            if i+1>=len(tokens) or tokens[i+1] in ("|","<",">"): raise ValueError("redirect")
            i+=1
            if token=="<":
                if len(stages)!=1 or source is not None: raise ValueError("input")
                source=tokens[i]
            else:
                if target is not None: raise ValueError("output")
                target=tokens[i]
        elif token in ("<<",">>","||","&&","&",";"): raise ValueError("unsupported operator")
        else: stages[-1].append(token)
        i+=1
    if not stages[-1]: raise ValueError("empty command")
    return stages,source,target
def run_line(line,timeout=5):
    stages,source,target=parse(line); processes=[]; deadline=time.monotonic()+timeout
    with contextlib.ExitStack() as stack:
        incoming=stack.enter_context(open(source,"rb")) if source else subprocess.DEVNULL
        outgoing=stack.enter_context(open(target,"wb")) if target else subprocess.PIPE
        try:
            for i,args in enumerate(stages):
                last=i==len(stages)-1
                process=subprocess.Popen(args,stdin=incoming,stdout=outgoing if last else subprocess.PIPE,shell=False)
                processes.append(process)
                if i>0: incoming.close()
                incoming=process.stdout
            output,_=processes[-1].communicate(timeout=max(.01,deadline-time.monotonic()))
            for process in processes[:-1]: process.wait(timeout=max(.01,deadline-time.monotonic()))
            return dict(stdout=(output or b"").decode("utf8"),returncodes=[p.returncode for p in processes])
        finally:
            for process in processes:
                if process.poll() is None: process.kill()
            for process in processes:
                process.wait()
                if process.stdout is not None: process.stdout.close()
def main():
    while True:
        try: line=input("pe> ")
        except EOFError: break
        if line.strip()=="exit": break
        if not line.strip(): continue
        try: print(run_line(line)["stdout"],end="")
        except (ValueError,OSError,subprocess.SubprocessError) as error: print(type(error).__name__,error)
if __name__=="__main__": main()
