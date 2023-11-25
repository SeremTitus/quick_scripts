import sys
import os
import subprocess
from queue import Queue

def gen_cmd(py_file_path):
    base_name = os.path.splitext(os.path.basename(py_file_path))[0]
    cmd_file_path = os.getcwd()+ '\\_'+ base_name + '.cmd'
    with open(cmd_file_path, 'w') as cmd_file:
        cmd_file.write('@echo off\n')
        cmd_file.write(f'python "{py_file_path}" %*')

    print(f'_{base_name} command has been created.')

def process_folder(folder_path, queue):
    python_files = [f.path for f in os.scandir(folder_path) if f.is_file() and f.name.endswith('.py')]
    for python_file in python_files:
        gen_cmd(python_file)
    try:
        subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir() and not f.name.startswith('.')]
        for subfolder in subfolders:
            queue.put(subfolder)
    except:
        print(f"Access is denied: {folder_path}")


starting_folder = os.path.dirname(sys.argv[0])

if len(sys.argv) > 1:
    starting_folder = os.getcwd()

folder_queue = Queue()
folder_queue.put(starting_folder)

while not folder_queue.empty():
    current_folder = folder_queue.get()
    process_folder(current_folder, folder_queue)