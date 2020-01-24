#NameError
#typeError


try:
    print(4+"hi")
    print(5/0)
except NameError:
    print("Variable is not defined")

except Exception as e:
    print(e)

