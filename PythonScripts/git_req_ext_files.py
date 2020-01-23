
import os
req_path=input("Enter your dir path: ")
if os.path.isfile(req_path):
    print(f"The given path {req_path} is a file. Please pass only the dir path ")
else:
    all_f_ds=os.listdir(req_path)
    if len(all_f_ds)==0:
        print(f"The given path is {req_path} is an empty path")
    else:
        req_ex=input("Enter the required files extensions .py .txt .md .sh: ")
        req_files=[]
        for each_f in all_f_ds:
            if each_f.endswith(req_ex):
                req_files.append(each_f)
        if len(req_files)==0:
            print(f"There are no files {req_ex} in the location of {req_path}")
        else:
            print(f"There are {len(req_files)} files in the location of {req_path} with an extension of {req_ex}")                
            print(f"So the files are: {req_files}")






