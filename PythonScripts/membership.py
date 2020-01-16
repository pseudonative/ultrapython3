# valid_java=['1.6','1.7','1.8','1.9']
# host_java="1.5"

# if host_java in valid_java:
#     print("host deployed of valid java version")
# else:
#     print("host deployed with invalid java version")


db_user=['db_admin','db_conf','db_installation']

random_user="db_conf"
if random_user in db_user:
    print("Yes this user is allowed to start db")
else:
    print('this user is not a valid user to start db')



