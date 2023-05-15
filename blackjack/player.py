class Player():
    def __init__(self):
        self.hand = []
        self.score = 0

    def get_score(self):
        '''
        Given the cards (embedded list) in the hand calculate the score of the hand,
        if aces are present and score is greater than 21 we will iteratively
        alter them to lower, returns score as an integer
        '''
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
        '''
        Print cards in hand neatly
        '''
        for i in self.hand:
            print(f'{i[1]} of {i[0]}')
