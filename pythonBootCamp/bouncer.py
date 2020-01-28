# ask for age
age=input("How old are you: ")

# if age:
#     age=int(age)
#     if age>=18 and age <21:
#         print("You can enter, but need a wristband!")
#     elif age>21:
#         print("You can enter and drink")
#     else:
#         print("you cannot come in little one")

# else:
#     print("please enter an age!")


if age:
    age=int(age)
    if age>=18:
        print("You can enter, but need a wristband!")
    elif age>=21:
        print("You can enter and drink")
    else:
        print("you cannot come in little one")

else:
    print("please enter an age!")