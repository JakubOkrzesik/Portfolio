class Music():
    def __init__(self):
        self.artist = 'Ed Sheeran'
        self.song = 'Hazard duty pay'
        self.album = 'Divide'
        self.year = '2017'
    
    def __str__(self):
        return 'Performer: ' + self.artist + '\n' + 'Song: ' + self.song + '\n' + 'Album: ' + self.album + '\n' + 'Year: ' + self.year

muzyka = Music()

print(muzyka)