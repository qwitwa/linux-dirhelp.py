import os
import sys
import re
from helpstring import helpstring

dirlist = []

def no_matches(path):
		print("No help found for", path)

for arg in sys.argv[1:]:
		if os.path.exists(arg):
				arg = os.path.abspath(arg)
				dirlist.append(arg)

if len(dirlist) == 0:
		dirlist.append(os.getcwd())

for path in dirlist:
		pathinfo = re.search(r"^%s\n(^/.*\n)*.*"%path, helpstring, re.M)
		if pathinfo is None:
				no_matches(path)
				break
		pathinfo = pathinfo.group(0)
		list_of_lines = pathinfo.split('\n')
		last_line = list_of_lines.pop()
		print(path)
		print(last_line)




