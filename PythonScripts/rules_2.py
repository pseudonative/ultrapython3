import re
text="isa python learn and itlearnis easy to"
# my_pat='^i[ts]'
# my_pat='learn$'
# my_pat=r'\blearn\b'
my_pat=r'\Blearn\B'
print(re.findall(my_pat,text))