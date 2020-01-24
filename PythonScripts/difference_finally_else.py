try:
    
    print(a)
except NameError:
    print("Variable is not defined")
except Exception as e:
    print("Exception occured:",e)
# finally:
#     print("This will execute always")
else:
    print("This will execute if ther is no exeptin in try block")

    
