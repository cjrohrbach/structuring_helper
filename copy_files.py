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


def copy_pdf(target_path, pdf_struct):
    file_name = pdf_struct['file_name']
    src_path = pdf_struct['path']
    shutil.copy(src_path, target_path + "/" + file_name)


def create_one_submission(eclipse_path, pdf_path,  submission_struct):

    eclipse_folder = create_folder(eclipse_path, submission_struct['name'])
    pdf_folder = create_folder(pdf_path, submission_struct['name'])

    src_folder = create_eclipse_project(submission_struct['name'], eclipse_folder)

    for java_struct in submission_struct['java_files']:
        copy_java(src_folder, java_struct)

    for pdf_struct in submission_struct['pdf']:
        copy_pdf(pdf_folder, pdf_struct)


def copy_files_to_structure(path, submission_array):
    eclipse_path = create_folder(path, "java")
    pdf_path = create_folder(path, "pdf")

    for submission in submission_array:
        create_one_submission(eclipse_path, pdf_path, submission)