from tkinter import filedialog

import helper_methods
from get_files import get_files
from copy_files import copy_files_to_structure
import os



if __name__ == '__main__':
    # path_to_structure = input('What is your name?\n')
    # target_path = input("Select the target path\n")

    file_path = filedialog.askdirectory(title="In Path")
    print("Path: ", file_path)
    res = get_files(file_path)

    out_path = filedialog.askdirectory(title="Out Path")

    copy_files_to_structure(out_path, res)


