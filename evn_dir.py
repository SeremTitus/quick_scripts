import os
current_path = os.environ.get('PATH', '')
new_directory = os.getcwd()
new_path = f'{current_path};{new_directory}'
os.environ['PATH'] = new_path
print(f'added {new_directory} to system environment variable PATH')