from player import Player
from card_deck import CardDeck


class Dealer(Player):

    def __init__(self):
        super().__init__("Dealer","Dealer")
        self.deck = CardDeck()

        return None

    def shuffle_deck(self):
        """
        >>> import random; random.seed(1)
        >>> dealer = Dealer()
        >>> dealer.shuffle_deck()
        >>> str(dealer.deck)[0:20]
        '10 8 10 6 8 9 3 10 2'
        """
        self.deck.shuffle()

        return None

    def signal_hit(self, player):
        """
        A method called by players when they want to hit
        Should deal one card to the player that signalled a hit

        >>> import random; random.seed(1)
        >>> dealer = Dealer()
        >>> dealer.shuffle_deck()
        >>> player = Player(None, None)
        >>> dealer.signal_hit(player)
        >>> player.hand
        [10]
        """
        player.deal_to(self.deck.draw())
        return None

    def play_round(self):
        """
        A dealer should hit if his hand totals to 16 or less

        >>> import random; random.seed(1)
        >>> dealer = Dealer()
        >>> dealer.shuffle_deck()
        >>> dealer.play_round()
        >>> dealer.hand
        [10, 8]
        """
        while (self.card_sum<=16):
            self.signal_hit(self)

        return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
