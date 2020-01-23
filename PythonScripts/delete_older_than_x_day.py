#!/usr/local/bin/python3.7
import os
import sys
import datetime
req_path=input("enter your path: ")
age=3
if not os.path.exists(req_path):
    print("Please provide valid path ")
    sys.exit(1)
if os.path.isfile(req_path):
    print("Please provide directory path ")
    sys.exit(2)

for each_file in os.listdir(req_path):
    each_file_path=os.path.join(req_path,each_file)
    if os.path.isfile(each_file_path):
        print(each_file_path,datetime.datetime._fromtimestamp(os.path.getctime()))





