import subprocess

def connectionIsWorking():
    p = subprocess.Popen(["ping", "-c", "1", "1.1.1.1", "-w1"], stdout=subprocess.PIPE)
    p.wait()

    if p.returncode == 0:
        return True
    return False
