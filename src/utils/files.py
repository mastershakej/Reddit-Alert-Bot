import os
from utils.dict_compare import dict_compare
from utils.logger import Logger

EMPTY = ''


def create_file(full_path):
    full_path = os.path.abspath(full_path)
    directory = os.path.dirname(full_path)
    if not os.path.exists(directory):
        Logger.log('Creating directory ' + directory)
        os.makedirs(directory)
    with open(full_path, 'w+') as f:
        f.close()


def read_file(full_path):
    with open(full_path, 'r') as f:
        contents = f.read()
        f.close()
        return contents


def write_to_file(full_path, string):
    with open(full_path, 'w') as f:
        f.seek(0)
        f.truncate()
        f.write(str(string))
        f.close()


def erase_contents(full_path):
    with open(full_path, 'w') as f:
        f.seek(0)
        f.truncate()
        f.close()


def is_empty(full_path):
    with open(full_path, 'r') as f:
        contents = f.read()
        f.close()
        if contents == EMPTY:
            return True
        return False
