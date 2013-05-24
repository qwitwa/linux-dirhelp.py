import os
import sys
import re
from helpstring import helpstring

dirlist = []
helplist = helpstring.split('\n')
for index, line in enumerate(helplist):
		if line == "": 		
				line = "\n"
		if line[0] == "$" or line[0] == "/":
				helplist[index] = os.path.expandvars(line)

def no_matches(path):
		print("No help found for", path)

def get_dir_info(path):
		for index, string in enumerate(helplist):
				if string == path:
						while True:
								if helplist[index][0] not in ["\n", "/", "$"]:
										return helplist[index]
								else:
										index += 1
		return None

for arg in sys.argv[1:]:
		if os.path.exists(arg):
				arg = os.path.abspath(arg)
				dirlist.append(arg)
		else:
				print(arg, "does not exist.")
				exit()

if len(dirlist) == 0:
		dirlist.append(os.getcwd())

for path in dirlist:
		pathinfo = get_dir_info(path)
		if pathinfo is None:
				no_matches(path)
				break
		print(path)
		print(pathinfo)




