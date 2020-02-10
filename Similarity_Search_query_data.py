
# coding: utf-8

# In[12]:


# coding: utf-8

import csv
import collections

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

user_input = input("Enter 20 Food Choices separated by comma ::")
query  = user_input.split(",")

#query = ["vegetable","Rice", "Fish","Beef","Mutton","Chicken","Pork","Bread","Lamb","Milk", "Cake","Juice","Fries","Coffee","Tea","Soft_Drinks","Apple","Banana","Orange","Grape"]
#query = ['Cake', 'Rice', 'vegetable', 'Mutton', 'Banana', 'Milk', 'Coffee', 'Grape', 'Fish', 'Bread', 'Fries', 'Soft_Drinks', 'Lamb', 'Orange', 'Juice', 'Beef', 'Tea', 'Apple', 'Pork', 'Chicken']

#query = ['Beef','vegetable','Rice','Fish']
#query = ['vegetable','Fish','Beef','Rice']

num_of_similar_object = 20
n_tilde = 10  #closest n_tilde ref per object

#generate query point rank list

#load ref data list
input_ref_file = "C:\\Users\\Nilufa\\Desktop\\Projects\\referece_data.csv"

query_ref_sfd_list = []
csvfile = open(input_ref_file,'r')
for ref_line in csv.reader(csvfile):
    ref_id = ref_line[0]            
    sfd = calculate_sfd(query, ref_line[1:])
    query_ref_sfd_list.append((ref_id, sfd))
csvfile.close()

n_query_ref_sfd_list = sorted(query_ref_sfd_list, key=takeDist)[0:n_tilde] #sort refs based on distance and then take closest n_tile ref points (r1,123) (r3,134)
q_closest_ref_seq = []                 #closest n_tilde ref point 
for item in n_query_ref_sfd_list:
    q_closest_ref_seq.append(item[0])  #take only the ref id [r1, r3] 
#print(q_closest_ref_seq)

#load mif list
input_mif_file = "C:\\Users\\Nilufa\\Desktop\\Projects\\mif.csv"
with open(input_mif_file, 'r') as file:
        reader = csv.reader(file)
        mif_list = list(reader)


accumulator_dict = {} #A
count = 1

for ref_id in q_closest_ref_seq:   #for each ro in RO [r-1-4, r-3-2]
    ref_id_pos_mif = int(ref_id.split("-")[1])  #from r-1-4 take 1
    ref_id_obj_dist_list = mif_list[ref_id_pos_mif-1][1:]   #r-1-4, o-1:1,o-4:2,o-7:1,o-9:2,o-12:2 pl= [o-1:1,o-4:2,o-7:1,o-9:2,o-12:2]

    for obj_pos in ref_id_obj_dist_list:      #for each object in pl= [o-1:1,o-4:2,o-7:1,o-9:2,o-12:2]
        obj = obj_pos.split(":")[0]           #obj = o-3 from o-3:2
        ref_pos = int(obj_pos.split(":")[1])       #ref_pos = 2 from o-3:2

        if obj not in accumulator_dict:    #if ao not in A
            ao = 0                         #ao = 0
            accumulator_dict[obj] = ao     #A={o-3:0}
Fries,Grape,Soft_Drinks,Chicken,Cake,Beef,Orange,Mutton,Rice,Fish,Tea,Milk,Pork,Bread,Juice,Lamb,Banana,Apple,Coffee,vegetable
        ao = accumulator_dict[obj]         #from A={o-3:0} get 0
        ao = ao + abs(count - ref_pos)
        accumulator_dict[obj] = ao
        count += 1
#print(accumulator_dict)

closest_object_q = sorted(accumulator_dict.items(), key=lambda x: x[1])

if len(closest_object_q) < num_of_similar_object:
    num_of_similar_object = len(closest_object_q)

#load input_data
input_data_file = "C:\\Users\\Nilufa\\Desktop\\Projects\\input_data.csv"
with open(input_data_file, 'r') as file:
  reader = csv.reader(file)
  input_data_list = list(reader)

print('\n')
print("Query Object : " + str(query))
print('\n')
print("Similar Objects:")

#get input data seq for closest object
for i in range(num_of_similar_object):
    obj_id = closest_object_q[i][0]      #o-3
    obj_id_pos = int(obj_id.split("-")[1]) Fries,Grape,Soft_Drinks,Chicken,Cake,Beef,Orange,Mutton,Rice,Fish,Tea,Milk,Pork,Bread,Juice,Lamb,Banana,Apple,Coffee,vegetable
    obj_data = input_data_list[obj_id_pos -1][1:]
    print(obj_id + " : " +str(obj_data))

