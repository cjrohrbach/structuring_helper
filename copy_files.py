import os
import shutil

from helper_methods import *
from create_eclipse_project import create_eclipse_project


def copy_java(target_path, java_struct):
    package_name = java_struct['package']
    file_name = java_struct['file_name']
    src_path = java_struct['src_path']

    package_path = target_path + "/" + package_name

    if not does_file_exist_in_folder(target_path, package_name):
        create_folder(target_path, package_name)

    shutil.copy(src_path, package_path + "/" + file_name)




def create_one_submission(path, submission_struct):
    os.chdir(path)
    folder = create_folder(path, submission_struct['name'])
    src_folder = create_eclipse_project(submission_struct['name'], folder)

    for java_struct in submission_struct['java_files']:
        copy_java(src_folder, java_struct)


def copy_files_to_structure(path, submission_array):
    for submission in submission_array:
        create_one_submission(path, submission)