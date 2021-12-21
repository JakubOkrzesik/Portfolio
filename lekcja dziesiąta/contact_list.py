class Contact_list:
    def __init__(self):
        self.list = []

    def contactadd(self, info):
        self.list.append(info.cname)
        self.list.append(info.cemail)
        self.list.append(info.ctelephone)

    def contactdisplay(self):
        
        final_content = ''
        
        for x in range(len(self.list) - 1):
            if x%3==0:
                final_content += '\n'
            final_content+=self.list[x]

            


