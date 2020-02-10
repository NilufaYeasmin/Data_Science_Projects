import random
import csv
import pandas as pd

input_data_file = "input_data.csv"

#load input data
with open(input_data_file, 'r') as file:
  reader = csv.reader(file)
  input_data_list = list(reader)
file.close()

N = 1000000
total_ref = 1000

ref_dict = {}

count = 1
while(len(ref_dict) < total_ref):
    rand_row_num = random.randint(0, N)
    data_seq_list = input_data_list[rand_row_num-1][1:]    
    
    if data_seq_list not in ref_dict.values():
        ref_id_key = "r" + "-" + str(count) + "-" + str(rand_row_num)
        ref_dict[ref_id_key] = data_seq_list
        print(count)            
        count += 1

output_ref_file_name = "referece_data.csv"
pd.DataFrame.from_dict(data=ref_dict, orient='index').to_csv(output_ref_file_name, header=False)