class TV():
    def __init__(self, name):
        self.tvname = name
        self.is_on = False
        self.channelnum = 1
        self.channel_list = []
        self.volume = 0

    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on and self.channelnum<=len(self.channel_list):
            print(f"Tv is on, channel {self.channelnum} ({self.channel_list[self.channelnum-1]})")
        elif self.is_on:
            print(f"Tv is on, channel {self.channelnum}")
        else:
            print("Tv is off")

    def set_channel(self, new_channel_num):
        self.channelnum = new_channel_num
    
    def set_channels(self, new_channelslist):
        self.channel_list = new_channelslist

    def show_channels(self):
        for x in range(len(self.channel_list)):
            print(str(x+1) + '.' + self.channel_list[x])



tv = TV('Samsung')
print(tv.tvname)
tv.show_status()
tv.turn_on()
tv.show_status()
tv.set_channel(5)
tv.show_status()
tv.show_status()
tv.set_channels(['TVP1', 'tvp2', 'TVN', 'Disney XD', 'Siematv', 'Bruh'])
tv.show_channels()
tv.show_status()
tv.set_channel(9)
tv.show_status()
tv.turn_off()


