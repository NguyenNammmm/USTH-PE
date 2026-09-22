import subprocess
import sys

def launch_report():
    completed = subprocess.run(
        [sys.executable, "report_child.py"],
        capture_output=True, text=True, timeout=2,
        shell=False
    )
    return {"stdout": completed.stdout.strip(),
            "returncode": completed.returncode}