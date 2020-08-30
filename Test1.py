import os
import sys
import subprocess

abs_file = sys.argv[1]
file_path, file = os.path.split(os.path.abspath(abs_file))
file_name, file_ext = os.path.splitext(file)

subprocess.call(["ffmpeg", "-loglevel", "quiet", "-i", abs_file, f"{file_path}\\{file_name}.mp4"], shell=False)
os.remove(abs_file)
