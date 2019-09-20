# create 4 directories in target_path
import os

def create_dir(target_path):
    for category in ['red', 'green', 'blue', 'other']:
        dir_path = os.path.join(target_path, category)
        os.mkdir(dir_path)
