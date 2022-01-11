class C():
    def __init__(self, text):
        self.text = text

    def m(self):
        for x in range(len(self.text)):
            for y in range(len(self.text)):
                if x==y:
                    continue

                if self.text[x]==self.text[y]:
                    return False
            
        return True


x = C('blue water')

print(x.m())