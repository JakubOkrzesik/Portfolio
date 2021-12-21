class University(): 
    # object constructor (__init__ method)
    def __init__(self, name, fullname):  
    # object states/attributes (fields)
        self.name = name  
        self.full = fullname
    # object bahaviors (methods)
    
    def print_name(self): 
        print(self.name)

    def set_name(self, name): 
        self.name = name

    def print_fullname(self):
        print(self.full)

    def set_fullname(self, full):
        self.full = full

uni = University('UJ','Uniwersytet Jagiellonski')

uni.print_name()
uni.print_fullname()
uni.set_name('AGH')
uni.set_fullname('Akadenia Górniczo Hutnicza')
uni.print_name()
uni.print_fullname()