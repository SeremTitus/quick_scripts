import sys
import os
import subprocess

def get_branch(branch_name):
    try:
        subprocess.check_output(['git', 'checkout','-b', str(branch_name)], cwd=os.getcwd(), stderr=subprocess.STDOUT, universal_newlines=True)
        subprocess.check_output(['git', 'pull', '--force', 'origin', str(branch_name)], cwd=os.getcwd(), stderr=subprocess.STDOUT, universal_newlines=True)
        print(f"Git get_branch and checkout {source}")
    except subprocess.CalledProcessError as e:
        print(f"Git get_branch and checkout ERROR : {e.output.splitlines()[0]}")

if len(sys.argv) < 2:
    print("add branch_name as arg")
else:
    get_branch(sys.argv[1])