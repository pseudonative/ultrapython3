import re 
text="""this is a string
this is second line end
this is third line end
asfasd this end"""

my_pat=r'end$'

print(re.findall(my_pat,text,re.M|re.I))

