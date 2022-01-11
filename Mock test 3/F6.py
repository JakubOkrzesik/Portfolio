from typing import Counter


class C():
    def __init__(self, logics):
        self.table = logics

    def m(self):
        counter = 0
        
        list_range = len(self.table) - 1

        for x in range(list_range):
            if x==0 or x==list_range:
                continue
            else:
                if self.table[x-1]!=self.table[x] and self.table[x]!=self.table[x+1]:
                    counter+=1

        return counter

x = C([True,False,True,False])

print(x.m())