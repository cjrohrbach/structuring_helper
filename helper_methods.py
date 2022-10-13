import os
import re
from zipfile import PyZipFile

project_root_split = re.split(r'/|\\', __file__)
project_root_folder_name = project_root_split[len(project_root_split)-1]

project_root = __file__[0: (len(__file__) - len(project_root_folder_name) - 1)]
print("__file__: ", __file__)
print("project root: ", project_root)


def create_folder(path, name):
    try:
        os.chdir(path)
        os.mkdir(name)
    except:
        print("Directory ", name, " already exists in " , path)
    finally:
        return path + "/" + name


def does_file_exist_in_folder(path, filename):
    os.chdir(path)
    content = os.listdir()
    return filename in content


def extract_zip_in_place(path):

    zip_name = re.split(r'/|\\', path)
    zip_name = zip_name[len(zip_name)-1]

    containing_folder = path[0:(len(path) - len(zip_name) - 1)]

    zip_name = zip_name.split(".")
    zip_name = zip_name[0]

    pzf = PyZipFile(path)
    extraction_folder = create_folder(containing_folder, zip_name)
    pzf.extractall(extraction_folder)
    return extraction_folder


