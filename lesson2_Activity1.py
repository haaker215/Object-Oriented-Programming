class IOString:
    def __init__(self):
        self.str1 = ""
    def get_string(self):
        self.str1 = input("Enter a String: ")
    def print_String(self):
        print("Result In Upper Case Letters: ",self.str1.upper())
a = IOString()
a.get_string()
a.print_String()