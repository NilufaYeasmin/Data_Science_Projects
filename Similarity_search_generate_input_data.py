import random
import pandas as pd
import numpy as np
import csv
import sys

object_dict = {}


word_list = ["vegetable","Rice", "Fish","Beef","Mutton","Chicken","Pork","Lamb","Bread","Milk", "Cake","Juice","Fries","Coffee"
            ,"Tea","Soft_Drinks","Apple","Banana","Orange","Grape"]

output_file_name = sys.argv[1]

# Generate N records using Permutation
start = int(sys.argv[2])
end = int(sys.argv[3])

total_line = (end - start) + 1

while len(object_dict) < total_line:                            
    obj= np.random.permutation(word_list).tolist()   #Return one permutation of word_list            
    if obj not in object_dict.values():
        obj_id_key = "o" + "-" + str(start)
        object_dict[obj_id_key] = obj           
        start += 1
pd.DataFrame.from_dict(data=object_dict, orient='index').to_csv(output_file_name, header=False)