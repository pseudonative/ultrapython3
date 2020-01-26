import re 
# text="This is a pythonnnn and python aaa haaaasfd xyzaaaaaaaa"
# # my_pat=r'\bpython{4}\b'
# my_pat=r'\bxyza{8}\b'
# print(re.findall(my_pat,text))


text="xaz asdfa sdf xaazz xaaaaaaa xaaaz xaaaaz"
my_pat=r'\bxa{2,4}z\b'
print(re.findall(my_pat,text))




