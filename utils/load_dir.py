import os
import importlib

def load_dir(dir_path: str):
    """
    The load_functions function iterates over all the files in the given directory.
    If a file is a Python file, it imports the module and retrieves the function with
    the same name as the module. Then, it stores the function in the functions dictionary
    with the module name as the key.
    :return: A dictionary of functions.
    """
    directory = {}
    for file in os.listdir(dir_path):
        if os.path.isfile(f'{dir_path}/{file}') and file.endswith('.py'):
            module_name = os.path.splitext(file)[0]
            module = importlib.import_module(f'{dir_path}.{module_name}')
            function = module.__dict__[module_name]
            directory[module_name] = function
    return directory
