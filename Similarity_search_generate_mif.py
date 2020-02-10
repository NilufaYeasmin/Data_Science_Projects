import random
import pandas as pd
import numpy as np
import csv
import sys

output_mif_file_name = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])

total_line = (end - start) + 1

#prepare partial ref_id list from full ref_data
input_ref_file = "referece_data.csv"
with open(input_ref_file, 'r') as file:
  reader = csv.reader(file)
  full_ref_data_list = list(reader)    #list of list

part_ref_id_list = []
for i in range(start -1, end):
	ref_id = full_ref_data_list[i][0]  #First element is the ref id
	part_ref_id_list.append(ref_id)

#load pruned data list
input_prune_data_file = "pruned_data.csv"
with open(input_prune_data_file, 'r') as file:
  reader = csv.reader(file)
  pruned_data_list = list(reader)

with open(output_mif_file_name, 'w') as writeFile:
	writer = csv.writer(writeFile)

	for ref_id in part_ref_id_list:                                #for each ref_id
		ref_obj_position_list = [ref_id]
		for data_obj in pruned_data_list:                          #for each data_object from pruned pruned_data_list
			if ref_id in data_obj:                                    #if ref_id is in pruned data list
				obj_id = data_obj[0]                               #first elemet in pruned data list is the object id
				ref_position = data_obj.index(ref_id)                 #get position of the ref in the pruned data list
				obj_id_ref_position = obj_id + ":" + str(ref_position)
				ref_obj_position_list.append(obj_id_ref_position)   #append obj and ref position e.g., (o1, 1) 
	
		writer.writerow(ref_obj_position_list)



