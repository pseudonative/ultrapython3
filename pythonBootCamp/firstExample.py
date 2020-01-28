name="Tomlin"
if name=="Arya Stark":
    print("Valar Morghulis")
elif name=="Jon Snow":
    print("You know nothing")
else:
    print("Carry on")

print("=================================")

from random import randint
choice=randint(1,10)

if choice==1:
    print("lucky")
else:
    print("unlucky")

print("=================================")


from random import randint
num=randint(1,1000)
if num % 2 !=0:
    print("odd")
else:
    print("even")
