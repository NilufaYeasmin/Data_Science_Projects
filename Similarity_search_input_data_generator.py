import csv
import pandas as pd
import subprocess
import os
import glob
import subprocess
from subprocess import Popen,PIPE
import time

N = 1000000
num_files = 10

num_line_per_file = int(N/num_files)
split_files_lists = []

procs_list = []
start = 1
end = num_line_per_file

for i in range(num_files):
	split_input_file = "input_data_" + str(i) + ".csv"
	split_files_lists.append(split_input_file)
	cmd = ['python','generate_input_data.py', split_input_file, str(start), str(end)]
	start = end + 1
	end = end + num_line_per_file
	procs_list.append(Popen(cmd, stdout=PIPE, stderr=PIPE))

for proc in procs_list:
    proc.wait()

cmd_run = "cat "
for split_input_file in split_files_lists:
	cmd_run += split_input_file + " "
cmd_run += "> "
cmd_run += "input_data.csv"

os.system(cmd_run)
print("Completed")