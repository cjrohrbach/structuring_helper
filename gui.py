import tkinter.messagebox
from tkinter import *
from tkinter import filedialog as fd
from tkinter.ttk import Style, Label

from split import split
from get_files import get_files
from copy_files import copy_files_to_structure

from helper_methods import create_folder

import os

def select_file(title):
    filename = fd.askdirectory(
        title=title,
        initialdir='./'
    )
    return filename

def do_unpacking(src_path, out_path):
    copy_files_to_structure(out_path, get_files(src_path))


class Tool:
    def __init__(self):
        win = Tk()
        win.title('Abgaben Tool')
        win.geometry("500x500")

        heading_style = Style(win)
        heading_style.configure("Heading", font=('Arial', 17))

        self.win = win

        self.setup_file_frame()
        self.setup_control_button_frame()
        self.setup_split_frame()

        execute = Button(win, text="Execute", command=self.execute)
        execute.pack(side=BOTTOM, pady=20)

        self.win.mainloop()

    def execute(self):
        self.src_path = self.src_entry.get()
        self.out_path = self.out_entry.get()




        if self.do_split.get():
            print("Do Split")
            try:
                num_of_ass = int(self.number_of_assistants.get())
            except:
                tkinter.messagebox.showerror(title="Error", message="Number of Assistants has to be an integer")
                return

            folder_template_name = self.folder_name.get()
            split(self.src_path, self.out_path, num_of_ass, folder_template_name)

        if self.do_unpack.get():
            print("Do Unpacking")
            self.unpack()


        print(self.src_path)
        print(self.out_path)
        tkinter.messagebox.showinfo(title="Done", message="Done")

    def unpack(self):
        if not self.do_split.get():
            # Simple unpacking if no split was performed before
            do_unpacking(self.src_path, self.out_path)
        else:
            os.chdir(self.out_path)
            split = os.listdir()
            print(split)
            for folder in split:
                folder_src_path = self.out_path + "/" + folder + "/Ilias/"
                folder_structured_path = create_folder(self.out_path + "/" + folder, "structured")
                try:
                    do_unpacking(folder_src_path, folder_structured_path)
                except:
                    tkinter.messagebox.showwarning(title="Some Error occured", message="There was an error unpacking the files")



    def setup_file_frame(self):
        """
        Setup the tkinter frame containing the utilites to choose files
        :return:
        """
        file_frame = Frame(self.win)

        src_label = Label(file_frame, text="Source Path")
        src_label.grid(column=0, row=0)

        src_entry = Entry(file_frame)
        src_entry.grid(column=1, row=0)
        self.src_entry = src_entry

        src_button = Button(file_frame, text="Choose", command=self.select_file_in)
        src_button.grid(column=2, row=0)

        out_label = Label(file_frame, text="Out Path")
        out_label.grid(column=0, row=1)

        out_entry = Entry(file_frame)
        out_entry.grid(column=1, row=1)
        self.out_entry = out_entry

        out_button = Button(file_frame, text="Choose", command=self.select_file_out)
        out_button.grid(column=2, row=1)

        file_frame.pack(pady=20)

    def setup_control_button_frame(self):
        control_frame = Frame(self.win)
        heading = Label(control_frame, text="What should be done?", style="Heading")
        heading.grid(column=0, row=0, columnspan=2)
        self.do_split = BooleanVar(value=False)
        split_box = Checkbutton(control_frame, text="Split", variable=self.do_split)
        split_box.grid(column=0, row=1)
        self.do_unpack = BooleanVar(value=True)
        unpack_box = Checkbutton(control_frame, text="Unpack Files", variable=self.do_unpack)
        unpack_box.grid(column=1, row=1)
        control_frame.pack(pady=20)

    def setup_split_frame(self):
        split_frame = Frame(self.win)
        Label(split_frame, text="Setup the Split:", style="Heading").grid(row=0, columnspan=2, column=0)

        Label(split_frame, text="Number of Assistants").grid(row=1, column=0)
        self.number_of_assistants = Entry(split_frame)
        self.number_of_assistants.insert(END,4)
        self.number_of_assistants.grid(row=1, column=1)
        Label(split_frame, text="Folder Naming").grid(row=2, column=0)
        self.folder_name = Entry(split_frame)
        self.folder_name.insert(END, "XX_Abgabe_")
        self.folder_name.grid(row=2, column=1)

        split_frame.pack(pady=20)



    def select_file_in(self):
        src_path = select_file("Source Path")
        self.src_entry.insert(END, src_path)


    def select_file_out(self):
        out_path = select_file("Out Path")
        self.out_entry.insert(END, out_path)

def main():
    tool = Tool()


main()