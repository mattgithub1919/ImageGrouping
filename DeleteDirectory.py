# delete directories that might be left over before
# Please note that it cannot delete folders named other than \\
# 'read', 'green', 'blue', 'other'
import os
import shutil

def del_dir(filespath):
    for category in ['red', 'green', 'blue', 'other']:
        dir_path = os.path.join(filespath, category)
        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)
