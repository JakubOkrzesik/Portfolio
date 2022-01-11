class C():
    def __init__(self, text):
        self.text = text
    
    def m1(self):
        dict = {}
        for x in self.text:
            if x not in dict:
                dict[x] = 1
            else:
                for y in dict.keys():
                    if x==y:
                        dict[x]+=1

        return dict

    def m2(self, keywords):
        
        newdict = {}
        
        for x in keywords:
            for y in C.m1(self).keys():
                if x==y:
                    newdict[y] = C.m1(self)[y]

        return newdict
    

x = C('my moon')

print(x.m2('mn'))