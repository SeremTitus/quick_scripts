import os
import subprocess
from queue import Queue

def git_pull(folder_path):
    try:
        subprocess.check_output(['git', 'pull'], cwd=folder_path, stderr=subprocess.STDOUT, universal_newlines=True)
        print(f"Git pull successful in {folder_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error in git pull for {folder_path} : {e.output.splitlines()[0]}")

def process_folder(folder_path, queue):
    if os.path.exists(os.path.join(folder_path, '.git')):
        git_pull(folder_path)
    else:
        try:
            subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]
            for subfolder in subfolders:
                queue.put(subfolder)
        except:
            print(f"Access is denied: {folder_path}")


starting_folder = os.getcwd()

folder_queue = Queue()
folder_queue.put(starting_folder)

while not folder_queue.empty():
    current_folder = folder_queue.get()
    process_folder(current_folder, folder_queue)
