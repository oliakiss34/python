class Mailing:
    
     def __init__(self, to_address, from_address, cost, track):
        self.adress = to_address
        self.faddress = from_address
        self.cost = cost
        self.track = track
    
    def to_address(self):
        print(self.to_address)

    
    def from_address(self):
        print(self.from_address)