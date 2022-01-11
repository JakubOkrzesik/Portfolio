class Samsung():
    def __init__(self):
        self.name = 'Samsung A7'
        self.year = '2018'
        self.screentype = 'LED display'

class Iphone():
    def __init__(self):
        self.name1 = 'Iphone 7'
        self.year2 = '2018'
        self.screentype3 = 'Retina display'



class Phones(Samsung, Iphone):
    def __init__(self):
        self.state = False
        self.phonename = ''
        self.phoneyear = ''
        self.phonescreen = ''
        
        Samsung().__init__(self)
        Iphone().__init__(self)


    def phoneselect(self):
        x = input('Please select your device by typing Samsung or Iphone: ')
        if x=='Samsung':
            self.phonename = self.name
            self.phoneyear = self.year
            self.phonescreen = self.screentype
        else: 
            self.phonename = self.name1
            self.phoneyear = self.year2
            self.phonescreen = self.screentype3
            
    def powertoggle(self):
        self.state = not self.state
        print(f'Phone power status: {self.state}')

    def showstatus(self):
        
        if self.state:
            return 'Name: ' + self.phonename + '\n' + 'Year: ' + self.phoneyear + '\n' + 'Screen type: ' + self.phonescreen

        else:
            return 'Phone is off. Turn the phone on first to display its characteristics'


phone = Phones()

phone.phoneselect()
phone.powertoggle()
print(phone.showstatus())