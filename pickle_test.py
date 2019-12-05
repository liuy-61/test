import pickle
import os
data_dir = '/home/lql/data'
os.chdir(data_dir)
dict_save = {'da':111, 2:[1,2,3], '23':{1:2, 'd':'happy'}}
# file = open('pickle.example','rb')
with open('pickle.example','rb') as file:
 var = pickle.load(file)
print(var)
