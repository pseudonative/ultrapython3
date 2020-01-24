import json 

# req_file="/home/jeremy/Documents/gitStuff/ultrapython3/PythonScripts/myjson.json"

# fo=open(req_file,'r')
# print(json.load(fo))




# fo.close()

my_dict={'Name':'Jeremy','Skills':['Python','Shell','GCS','AWS']}

req_file="myinfo.json"

fo=open(req_file,'w')

json.dump(my_dict,fo,indent=4)

fo.close()






