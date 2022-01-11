class C():
    def __init__(self, number):
        self.number = number

    def m(self):
        try:
            x = int(self.number['value'], int(self.number['system']))
            return x

        except:
            return -1


x = C({"system":"8", "value":"70281"})


print(x.m())