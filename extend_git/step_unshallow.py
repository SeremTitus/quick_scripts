import sys
import os
import subprocess

try:
    start_var = int(subprocess.check_output(['git', 'rev-list', 'HEAD', '--count'], cwd=os.getcwd(), stderr=subprocess.STDOUT, universal_newlines=True))
    max_var = start_var + 5
    if len(sys.argv) >= 2:
        max_var = start_var + int(sys.argv[1])
    while (True):
        start_var += 1
        print(start_var)
        if start_var > max_var:
            break
        try:
            subprocess.check_output(['git', 'fetch', '--depth', str(start_var)], cwd=os.getcwd(), stderr=subprocess.STDOUT, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            print(f"ERROR : {e.output.splitlines()[0]}")
            break
    print("Done: new depth = " + subprocess.check_output(['git', 'rev-list', 'HEAD', '--count'], cwd=os.getcwd(), stderr=subprocess.STDOUT, universal_newlines=True))
except subprocess.CalledProcessError as e:
    print(f"ERROR : {e.output.splitlines()[0]}")