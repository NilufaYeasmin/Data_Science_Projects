import csv
import pandas as pd
import subprocess
import os
import glob
from subprocess import Popen,PIPE

N = 1000000
num_files = 10

procs_list = []

#input_data_file = "input_data.csv"
#Split input file into smaller files 
#line_per_file = str(int(N/num_files))
#subprocess.call(["split", "-l", line_per_file, input_data_file, "split_file_", "-d"])
#split_file_list = glob.glob('split_file_*')
#procs_list = []
#for split_file_name in split_file_list:
#   cmd = ['python','generate_prune_list.py', split_file_name]
#   procs_list.append(Popen(cmd, stdout=PIPE, stderr=PIPE))

output_pruned_split_files_list = []

for i in range(num_files):
    
    input_split_file_name = "input_data_" + str(i) + ".csv"
    
    output_pruned_split_file_name = "pruned_data_" + str(i) +".csv"
    output_pruned_split_files_list.append(output_pruned_split_file_name)

    cmd = ['python','generate_prune_list.py', input_split_file_name, output_pruned_split_file_name]
    procs_list.append(Popen(cmd, stdout=PIPE, stderr=PIPE))

for proc in procs_list:
    proc.communicate()


#Mergeall split prune file into one
cmd_run = "cat "
for split_prune_file in output_pruned_split_files_list:
    cmd_run += split_prune_file + " "
cmd_run += "> "
cmd_run += "pruned_data.csv"

os.system(cmd_run)
print("Completed")