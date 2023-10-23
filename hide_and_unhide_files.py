import os

os.system("title Keep your files private - Harrison")
os.system("color a")

def file_path_collector():
	global file_path, file_list
	file_path = input("Enter the file path to be worked on \n(YOU CAN SEPERATE MULTIPLE FILE PATHS WITH A DOUBLE SPACE): ")

	file_list = list(file_path.split("  "))
	def file_list_filter():
		global file_list
		file_list = file_list
		global job
		try:
			for file in file_list:
				data = open(file)
		except FileNotFoundError:
			if len(file_list) > 1:
				file_list.remove(file)
				print(f"{file} wasn't found and has been deleted from the batch.\n")
				file_list_filter()
			else:
				print(f"{file} wasn't found. Enter a valid file path.\n")
				file_path_collector()
		else:
			job = input("\nWhat do you want to do to the specified file(s)?\n 1. Hide file(s)\n 2. Unhide file(s)\n Please enter the appropriate number: ")
	file_list_filter()
file_path_collector()

if job == "1":
	for file in file_list:
		os.system('attrib +s +h "' + file + '"')
	

if job == "2":
	for file in file_list:
		os.system('attrib -s -h "' + file + '"')

os.system("pause")