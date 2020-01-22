import os
path="/home/jeremy/Documents/gitStuff/ultrapython3/PythonScripts"
# print(list(os.walk(path)))
print("---------------------------")
for r,d,f in os.walk(path):
    if len(f) !=0:
        print(r)
        for each_file in f:
            print(os.path.join(r,each_file))
        print("---------------------------")