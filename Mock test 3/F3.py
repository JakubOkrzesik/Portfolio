class C():
    def __init__(self, *names):
        self.names = names

    def m(self):
        for x in range(len(self.names[0])):
            for y in range(len(self.names[0])):
                if x==y:
                    continue
                elif self.names[0][x].lower()==self.names[0][y].lower():
                    return True

        return False


    def siema(self):
        print(self.names[0][1])

x = C(['anna','ANNA'])

print(x.m())