import json

class C():
    def __init__(self, filename):
        self.jsondata = filename

    def m(self,n1,n2):
        with open(self.jsondata, 'r') as f:
            data = json.load(f)

            
            with open('mockdata1.json', 'w') as w:

                data1 = [x for x in data if x['wife']['age']>=n1 and len(x['children'])>=n2]
                
                json.dump(data1, w)

                
                        

    



x = C('mockdata.json')

x.m(40,1)
        

