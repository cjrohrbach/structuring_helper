from xml.dom import minidom
import os
from helper_methods import *
import shutil

def create_dot_project(name, path):
    project_xml = minidom.parse(project_root + "/static/project_template.xml")
    name_element = project_xml.getElementsByTagName('name')[0].firstChild

    name_element.data = name

    f = open(path + "/.project", "w")
    project_xml.writexml(f)
    f.close()

def copy_class_path(path):
    shutil.copy(project_root+"/static/classpath.xml", path + "/.classpath")




def create_eclipse_project(name, path):
    create_dot_project(name, path)
    copy_class_path(path)
    src = create_folder(path, "src")
    create_folder(path, "bin")
    return src # return the src folder
