import csv
import pandas as pd
import sys

def takeDist(elem):
   return elem[1]

def calculate_sfd(a,b):
    temp_dict = {}
    rank_a = []
    rank_b = []
    
    for i in range(len(a)):
        key = a[i]
        value = i+1
        temp_dict[key] = value
        rank_a.append(value)
    
    for i in range(len(b)):
        rank_b.append(temp_dict[b[i]])
    
    sfd = 0
    for i in range(len(rank_a)):
        sfd += abs(rank_a[i] - rank_b[i])
        
    return sfd

input_data_file = sys.argv[1]
output_pruned_list_file = sys.argv[2]
input_ref_file = "referece_data.csv"

#load ref data list
with open(input_ref_file, 'r') as file:
  reader = csv.reader(file)
  ref_data_list = list(reader)
file.close()

#n_tilde = len(ref_data_list)
n_tilde = 10

with open(output_pruned_list_file, 'w') as writeFile:
    writer = csv.writer(writeFile)

    with open(input_data_file, "r") as readFile:
        reader = csv.reader(readFile)

        for i, obj_line in enumerate(reader):            
            obj_id = obj_line[0]        
            ref_sfd_list = []
            
            output_pruned_list = [obj_id]

            for ref_line in ref_data_list:
                ref_id = ref_line[0]            
                sfd = calculate_sfd(obj_line[1:], ref_line[1:])
                ref_sfd_list.append((ref_id, sfd))            
                
            n_ref_sfd_list = sorted(ref_sfd_list, key=takeDist)[0:n_tilde] #sort refs based on distance and then take closest n ref points        
            
            for item in n_ref_sfd_list:
                output_pruned_list.append(item[0])  #take only the ref id            

            writer.writerow(output_pruned_list)
