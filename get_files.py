import os
import sys
import json
from helper_methods import *

def crawl_folder(path, res):
	# print("current path: ", os.getcwd())
	# print("Path to crawl: ", path)
	if not os.path.isdir(path):
		return
	else:
		os.chdir(path)
		# print("New current path: ", os.getcwd())
		content = os.listdir()
		for c in content:
			c_path = path + "/" + c
			# print("c_path: ", c_path)
			# print("c_path is folder: ", os.path.isdir(c_path))

			c_split = c.split(".")
			c_ending = c_split[len(c_split) - 1]

			if c_ending == "zip":
				# if it's a zip, extract it and set c_path to the extracted content
				c_path = extract_zip_in_place(c_path)

			if os.path.isdir(c_path):
				crawl_folder(c_path, res)

			else:

				# print("Ending: ", c_ending)
				if c_ending == "pdf":
					res['pdf'].append({"file_name": c,"path": c_path})

				if c_ending == "java":
					# print("found java ", c_path)

					path_split = path.split("/")
					package = path_split[len(path_split)-1]  # The last folder in the path is the package
					if package == "src":
						package = ""


					j_struct = {
						"file_name": c,
						"src_path": c_path,
						"package": package
					}
					res['java_files'].append(j_struct)

		return





def get_files(root_path):
	os.chdir(root_path)
	root = os.listdir()
	res = []
	for abgabe in root:
		path = root_path + '/' + abgabe

		print("Sub folder: ", abgabe)
		if os.path.isdir(path):
			os.chdir(path)
			content = os.listdir()

			structure = {
				"name": abgabe,
				"java_files": [],
				"pdf": []
			}

			crawl_folder(path, structure)
			res.append(structure)

	print(json.dumps(res, indent=4))
	return res