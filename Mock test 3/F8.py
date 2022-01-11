from typing import Counter
import xml.etree.ElementTree as ET



class C():

    def __init__(self, filename):
        self.xml = filename




    def m(self,n1,n2):
        
        tree = ET.parse(self.xml)

        root = tree.getroot()

        counter = 0
        
        for x in range(len(root)):
            if int(root[x][2][1].text)>=n1 and len(root[x][3])>=n2:
                counter+=1

        return counter


x = C('mockdata.xml')

print(x.m(50,1))