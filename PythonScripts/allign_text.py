import os
t_w=os.get_terminal_size().columns

given_str=input("Entere your string: ")
print(given_str)
usr_cnf=input("Do you want to allign test: say yes or no ? ")
if usr_cnf=="no":
    print(given_str.center(t_w).title())
    print(given_str.ljust(t_w).title())
    print(given_str.rjust(t_w).title())



