class Employee:
    def __init__(self):
        print("Emplyee Created")
    def __del__(self):
        print("Destructer called!")
def create_obj():
    print("Making Object")
    obj = Employee()
    print("Fuction End...")
    return obj
print("Calling Fucntion....")
print("..Loading..")
print("Function Called")
obj = create_obj()
print()
print("Programe End")