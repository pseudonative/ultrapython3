# usr_str=input("enter your string: ")
# usr_action=input("enter your action on your string (valid actins are: lower/upper/title): ")
import sys
usr_str=sys.argv[1]
usr_action=sys.argv[2]

if usr_action=="lower":
    print(usr_str.lower())
elif usr_action=="upper":
    print(usr_str.upper())
elif usr_action=="title":
    print(usr_str.title())
else:
    print("your option is ivalid. Please select valid option lower/upper/title): ")   





