import os
from pathlib import Path

# os.rmdir('dir')  # OSError: [WinError 145] Папка не пуста: 'dir'
# Path('some_dir').rmdir()  # OSError: [WinError 145] Папка не пуста: 'some_dir'
os.rmdir('dir/other_dir/new_os_dir')
Path('some_dir/dir/new_Path_dir').rmdir()
