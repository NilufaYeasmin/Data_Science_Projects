import csv
import pandas as pd
import subprocess
import os
import glob
from subprocess import Popen,PIPE

input_ref_file = "referece_data.csv"

N = 1000000

total_ref = 1000
num_mif_split_files = 10
line_per_mif_split_files = int(total_ref/num_mif_split_files)

procs_list = []

output_mif_split_files_list = []
start = 1
end = line_per_mif_split_files

for i in range(num_mif_split_files):
    
    output_mif_split_file_name = "mif_" + str(i) +".csv"
    output_mif_split_files_list.append(output_mif_split_file_name)

    cmd = ['python','generate_mif.py', output_mif_split_file_name, str(start), str(end)]
    start = end + 1
    end = end + line_per_mif_split_files	
    procs_list.append(Popen(cmd, stdout=PIPE, stderr=PIPE))

for proc in procs_list:
    proc.communicate()


#Mergeall split prune file into one
cmd_run = "cat "
for output_mif_split_file_name in output_mif_split_files_list:
    cmd_run += output_mif_split_file_name + " "
cmd_run += "> "
cmd_run += "mif.csv"

os.system(cmd_run)
print("Completed")