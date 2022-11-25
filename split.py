import os
import math
import shutil
import numpy as np
from tkinter import filedialog

from helper_methods import create_folder


def split(in_path, out_path, number_of_assistants, folder_template):
    # go to the in folder
    os.chdir(in_path)
    # get all submissions alphabetically sorted
    submissions = sorted(os.listdir())
    # split the submissions evenly
    sub_split = np.array_split(submissions, number_of_assistants)

    assistant_ctr = 0
    for split in sub_split:
        split_name = folder_template + str(assistant_ctr)
        assistant_ctr += 1
        # create the split folder
        split_folder = create_folder(out_path, split_name)

        # copy the respective submissions to the split folder
        for sub in split:
            shutil.copytree(in_path + "/" + sub, split_folder + "/Ilias/" + sub)




if __name__ == '__main__':
    #in_path = filedialog.askdirectory(title="In Path")
    #print(in_path)
    in_path = "/Users/cyrillrohrbach/Desktop/Abgabe_Simulation/Serie 04/Abgaben"
    # out_path = filedialog.askdirectory(title="Out Path")
    # print(in_path)
    out_path = "/Users/cyrillrohrbach/Desktop/Abgabe_Simulation/Split"

    split(in_path, out_path, 4, "04_Abgabe_")

