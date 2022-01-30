class winnerStatus:

    def __init__(self, isWinner, position, whoWon):
        self.isWinner = isWinner
        self.position = position
        self.whoWon = whoWon
    def asdict(self):
        return {'isWinner': self.isWinner, 'position': self.position, 'whoWon': self.whoWon}