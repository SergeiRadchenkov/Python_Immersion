import os
from pathlib import Path

os.makedirs('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_Path_dir').mkdir()  # FileNotFoundError: [WinError 3] Системе не удается найти указанный путь: 'some_dir\\dir\\new_Path_dir'
Path('some_dir/dir/new_Path_dir').mkdir(parents=True)