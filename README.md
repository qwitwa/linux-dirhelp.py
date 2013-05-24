#A python clone of linux-directory-help

Original project by jrenner [here](https://github.com/jrenner/linux-directory-help).  
Port to C by Jakash3 [here](https://github.com/Jakash3/linux-dirhelp).
  
The helpstring included in helpstring.py takes the format of elements separated by newline characters. Lines starting with "/" or "$" have environment variables expanded. Newlines are ignored. When the program is run, after checking that all directories specified exist, the processed version of the helpstring is searched through to find a line equal to the specified path. If this is found, the next line which isn't an unsuccessfully expanded environment variable or a path is returned and printed.
