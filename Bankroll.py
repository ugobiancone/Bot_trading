class bankroll:
    def __init__(self, bank):
        self.bank = bank
    
    def buy(self):
        self.bank -= 100
    
    def sell(self, amount):
        self.bank += amount

    def get_bank(self):
        return self.bank
    
    