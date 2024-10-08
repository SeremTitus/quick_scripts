import sys
import os
import subprocess

try:
    branch_name = subprocess.check_output(
        ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
        cwd=os.getcwd(),
        stderr=subprocess.STDOUT,
        universal_newlines=True
    ).strip()
    remote_size = subprocess.check_output(['git', 'rev-list', 'origin/'+str(branch_name), '--count'], cwd=os.getcwd(), stderr=subprocess.STDOUT, universal_newlines=True)
    print("Remote size = " + remote_size)
    start_var = int(subprocess.check_output(['git', 'rev-list', 'HEAD', '--count'], cwd=os.getcwd(), stderr=subprocess.STDOUT, universal_newlines=True))
    max_var = start_var + 5
    if len(sys.argv) >= 2:
        max_var = start_var + int(sys.argv[1])
    while (True):
        start_var = int(subprocess.check_output(['git', 'rev-list', 'HEAD', '--count'], cwd=os.getcwd(), stderr=subprocess.STDOUT, universal_newlines=True))
        if (start_var > max_var):# or (start_var > int(remote_size)):
            break
        start_var += 1
        try:
            subprocess.check_output(['git', 'fetch', '--depth', str(start_var)], cwd=os.getcwd(), stderr=subprocess.STDOUT, universal_newlines=True)
            print(start_var)
        except subprocess.CalledProcessError as e:
            print(f"ERROR : {e.output.splitlines()[0]}")
            # break
    print("Done: new depth = " + subprocess.check_output(['git', 'rev-list', 'HEAD', '--count'], cwd=os.getcwd(), stderr=subprocess.STDOUT, universal_newlines=True))
except subprocess.CalledProcessError as e:
    print(f"ERROR : {e.output.splitlines()[0]}")