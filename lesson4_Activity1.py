class MyClass:
    __priVar = 27
    def __privMeth(self):
        print("I am inside the private method")
    def hello(self):
        print(MyClass.__priVar)
foo = MyClass()
foo.hello()
print(MyClass.__privMeth)
