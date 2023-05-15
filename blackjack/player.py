class Player():
    def __init__(self):
        self.hand = []
        self.score = 0

    def get_score(self):
        self.score = 0
        for card in self.hand:
            if isinstance(card[1], int):
                self.score += card[1]
            elif card[1] == 'Ace' and card[2] == 'H':
                self.score += 11
            elif card[1] == 'Ace' and card[2] == 'L':
                self.score += 1
            else:
                self.score += 10
        if self.score > 21:
            for card in self.hand:
                if card[1] == 'Ace' and card[2] == 'H':
                    card[2] = 'L'
                    return self.get_score()
        return self.score

    def print_hand(self):
        for i in self.hand:
            print(f'{i[1]} of {i[0]}')
