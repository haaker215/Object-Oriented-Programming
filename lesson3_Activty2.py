class person:
    def __init__(self,name,id_number):
        self.name = name
        self.id_number = id_number
    def display(self):
        print("The name of the person is ",self.name)
        print("The Id number of the person is ",self.id_number)
class employee(person):
    def __init__(self,name,post,salary,id_number):
        self.salary = salary
        self.post = post
        person.__init__(self,name,id_number)
a =employee("Ahmed","manager",1000000,303)
print(a.name)
print(a.post)
print(a.salary)
print(a.id_number)
