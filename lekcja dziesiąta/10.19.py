import statistics

class Statistics:
    def __init__(self):
        self.nums = []
        self.numsmax = 0
        self.numsmin = 0
        self.numsmean = 0
        self.numsmedian = 0
    
    def numsenter(self):
        while True:
            x = input('Please enter your numbers. Enter "q" to end the process: ')
            
            if x=='q':
                break
            else:
                self.nums.append(int(x))

        

    def nummedian(self):
        self.nums.sort()
        
        
        x = len(self.nums)//2

        if x%2==0:
            self.numsmedian = self.nums[x]
        else:
            self.numsmedian = (self.nums[x]+self.nums[x-1])/2
        
            
    def nummean(self):
        self.numsmean = statistics.mean(self.nums)
    
    def nummax(self):
        self.numsmax = max(self.nums)

    def nummin(self):
        self.numsmin = max(self.nums)

    def displaynums(self):
        for x in self.nums:
            print(x, end=' ')

    def displayall(self):
        print(f'Greatest number is: {self.numsmax}')
        print(f'Smallest number is: {self.numsmin}')
        print(f'The mean of the numbers is: {self.numsmean}')
        print(f'The median of the numbers is: {self.numsmedian}')
    
stats = Statistics()
stats.numsenter()
stats.displaynums()
stats.nummax()
stats.nummin()
stats.nummean()
stats.nummedian()
stats.displayall()