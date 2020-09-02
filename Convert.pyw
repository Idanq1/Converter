import os
import sys
import subprocess

abs_file = sys.argv[-1]
new_ext = sys.argv[1]
file_path, file = os.path.split(os.path.abspath(abs_file))
file_name, file_ext = os.path.splitext(file)

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

subprocess.call(["ffmpeg", "-loglevel", "quiet", "-y", "-i", abs_file, f"{file_path}\\{file_name}.{new_ext}"], startupinfo=si)
os.remove(abs_file)
