import glob
import shutil
# import os


class GetPyFiles:
    # Class Variables
    PATH = r'\Users\rdelamerced\PycharmProjects\pythonNotes\my_project_sample\Python_Algorithms'
    T_PATH = rf'/Users/rdelamerced/PycharmProjects/Target_Folder'

    """Moving All Python Files from 1 path dir to another path dir"""
    def __init__(self, dir_path=''):
        self.py_file = r'*.py'
        self._dir_path = rf'{dir_path}\{self.py_file}'
        self.py_list = glob.glob(self._dir_path)

    def __repr__(self):
        return f'Sample Absolute Path Names:\n' \
               f'Origin: \n' \
               r'\Users\rdelamerced\PycharmProjects\Target_Folder' \
               f'\nDestination: \n' \
               r'\Users\rdelamerced\PycharmProjects\Sample_Folder' \
               f'\n'

    def copy(self, origin=PATH, des=T_PATH):
        py_origin = f'{origin}/{self.py_file}'
        self.py_list = glob.glob(py_origin)
        for i, ele in enumerate(self.py_list[:]):
            shutil.copy(ele, des)
        print(f'\nPython Files from:\n{origin} ---> {des}\nSuccessfully Copied')

    def move(self, origin=PATH, des=T_PATH):
        py_origin = f'{origin}/{self.py_file}'
        self.py_list = glob.glob(py_origin)
        for i, ele in enumerate(self.py_list):
            shutil.move(ele, des)
        print(f'\nPython Files from:\n{origin} ---> {des}\nSuccessfully Moved')


if __name__ == '__main__':
    # Client Variables
    # folder = 'Python_Algorithms'
    # PATH = r'\Users\rdelamerced\PycharmProjects\pythonNotes\my_project_sample\Python_Algorithms'
    # TARGET_PATH = rf'/Users/rdelamerced/PycharmProjects/Target_Folder'

    # Instantiation
    gpf = GetPyFiles()

    # User Input Paths
    print(gpf)
    origin_path = input('Type absolute path for origin: ')
    des_path = input('Type absolute path for destination: ')

    # Commands
    gpf.copy(origin_path, des_path)

