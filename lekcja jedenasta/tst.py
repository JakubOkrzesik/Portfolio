from SMS import SMS

class siema(SMS):
    def __init__(self,s,r):
        super().__init__(sender = s, recipient = r)