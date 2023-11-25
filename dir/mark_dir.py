import sys
import os
def gen_cmd(shorthand):
    cmd_file_path ='\\_'+ shorthand + '.cmd'
    with open(cmd_file_path, 'w') as cmd_file:
        cmd_file.write('@echo off\n')
        cmd_file.write(f'cd "{os.getcwd()}"')

    print(f'_{shorthand} command has been created.')

if len(sys.argv) < 2:
    print("add shorthand as arg")
else:
    gen_cmd(sys.argv[1])