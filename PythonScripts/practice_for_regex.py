import re 
# text="This is a python2. and 4 it @ is . easy -to _ learn_@ python3"
# # my_pat="i[ts]"
# my_pat="[@as]"
# print(re.findall(my_pat,text))
# print(len(re.findall(my_pat,text)))
# print(re.findall("is","This is a python and it is easy to learn"))

# my_pat="[a-d]"
# print(re.findall(my_pat,text))


# my_pat="\w\w\w"
# print(re.findall(my_pat,text))

# my_pat="\W"
# print(re.findall(my_pat,text))

# my_pat="python\d"
# my_pat="\d\d"
# print(re.findall(my_pat,text))

# my_pat="\."
# print(re.findall(my_pat,text))

text="This is my ip of a db server: 255.100.102.103"
pat="\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"
print(re.findall(pat,text))


