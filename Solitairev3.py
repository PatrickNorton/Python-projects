class card:
    def __init__(self, number, suit, faceup):
        self.NUMBER = number
        self.SUIT = suit
        self.faceup = faceup

    def __str__(self):
        return str(self.NUMBER if self.NUMBER < 10 else 'tjqk'[self.NUMBER-10])+'♠♣♡♢'['schd'.index(self.SUIT)]

class pile:
    def __init__(self):
        self.pile = []
        