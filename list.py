import os
import sys

def list_cmd_files(directory):
    cmd_files = [file for file in os.listdir(directory) if file.endswith(".cmd")]
    return cmd_files

directory_path = os.path.dirname(sys.argv[0])

cmd_files = list_cmd_files(directory_path)

for cmd_file in cmd_files:
    print(cmd_file[:-4])