import subprocess

def connectionIsWorking():
    p = subprocess.Popen(["ping", "-c1", "1.1.1.1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()

    if p.returncode == 0:
        return True 

    print("Failed to ping Google, assuming that there's no internet connection.")
    return False
