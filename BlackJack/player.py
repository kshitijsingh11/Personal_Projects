import random


class Player:

    def __init__(self, name, dealer):
        self.name = name
        self.dealer = dealer
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.hand = []

        return None

    def decide_hit(self):
        return random.choice([True, True, False])

    def deal_to(self, card_value):
        """
        >>> player = Player(None, None)
        >>> player.deal_to(11)
        >>> player.hand
        [11]
        >>> player.deal_to(10)
        >>> player.hand
        [11, 10]
        """

        self.hand.append(card_value)  #Adds the card value to the players hand)
        return None

    @property
    def card_sum(self):
        """
        >>> player = Player(None, None)
        >>> player.deal_to(2)
        >>> player.card_sum
        2
        >>> player.deal_to(10)
        >>> player.card_sum
        12
        """
        sum = 0
        for i in range(len(self.hand)):
            sum = sum + self.hand[i]      #Finds the sum of the cards

        return sum

    def play_round(self):
        """
        >>> from dealer import Dealer
        >>> import random; random.seed(1)
        >>> dealer = Dealer()
        >>> dealer.shuffle_deck()
        >>> player = Player(None, dealer)
        >>> player.play_round()
        >>> player.hand
        [10]
        >>> player.play_round()
        >>> player.hand
        [10]
        >>> player.play_round()
        >>> player.hand
        [10, 8, 10]
        >>> player.play_round()
        >>> player.hand
        [10, 8, 10]
        """
        while (self.decide_hit()):
            if self.card_sum<21:
                self.deal_to(self.dealer.deck.draw())   #if the player decides to hit checking if the sum is less than 21 and then drawing another card.

            else:
                break
        return None

    def discard_hand(self):
        """
        >>> player = Player(None, None)
        >>> player.deal_to(11)
        >>> player.deal_to(5)
        >>> player.discard_hand()
        >>> player.hand
        []
        """
        self.hand.clear()   #discarding all the cards in one's hand

        return None

    @property
    def wins(self):
        return self.__wins

    @property
    def ties(self):
        return self.__ties

    @property
    def losses(self):
        return self.__losses

    @wins.setter
    def wins(self, w):
        self.__wins = w

    @ties.setter
    def ties(self, t):
        self.__ties = t

    @losses.setter
    def losses(self, l):
        self.__losses = l

    def record_win(self):
        """
        >>> player = Player(None, None)
        >>> player.record_win()
        >>> player.wins
        1
        """
        self.wins = self.wins + 1
        return None

    def record_loss(self):
        """
        >>> player = Player(None, None)
        >>> player.record_loss()
        >>> player.losses
        1
        """
        self.losses = self.losses + 1
        return None

    def record_tie(self):
        """
        >>> player = Player(None, None)
        >>> player.record_tie()
        >>> player.ties
        1
        """
        self.ties = self.ties + 1
        return None

    def reset_stats(self):
        """
        >>> player = Player(None, None)
        >>> player.record_tie()
        >>> player.record_loss()
        >>> player.record_win()
        >>> player.reset_stats()
        >>> player.ties
        0
        >>> player.wins
        0
        >>> player.losses
        0
        """
        self.ties = 0
        self.wins = 0
        self.losses = 0

        return None

    def __repr__(self):
        """
        Output should include the player name, their current hand, and their wins/ties/losses in that order
        >>> player = Player("Eric", None)
        >>> player.record_loss()
        >>> player.record_win()
        >>> player.record_win()
        >>> player
        Eric: [] 2/0/1
        """
        handStr = "["
        for i in range(len(self.hand) - 1):
            handStr = handStr + str(self.hand[i]) + ", "

        if len(self.hand) > 0:
            handStr = handStr + str(self.hand[len(self.hand) - 1])
        handStr = handStr + "] "
        rep = self.name + ": " + handStr + str(self.wins) + "/" + str(self.ties) + "/" + str(self.losses)
        return rep


if __name__ == "__main__":
    import doctest
    doctest.testmod()
