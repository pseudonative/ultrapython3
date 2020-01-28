# from random import randint
# x=randint(-100,100)
# while x==0:
#     x=randint(-100,100)
# y=randint(-100,100)
# while y==0:
#     y=randint(-100,100)

# if x>0 and y>0:
#     print("both positive")
# elif x<0 and y<0:
#     print("both negative")
# elif x>0 and y<0:
#     print("x is positive and y is negative")
# else:
#     print("y is positive and x is negative")


from random import choice,randint
actually_sick=choice([True,False])
kinda_sick=choice([True,False])
hate_your_job=choice([True,False])
sick_days=randint(0,10)

calling_in_sick=False 

if actually_sick and sick_days>0:
    calling_in_sick=True
elif kinda_sick and hate_your_job and sick_days>0:
    calling_in_sick=True
else:
    calling_in_sick=False



