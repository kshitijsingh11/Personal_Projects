
from player import Player
from dealer import Dealer


class BlackjackGame:
    def __init__(self, player_names):
        self.dealerObj = Dealer()  #representing dealer as an object
        self.player_list = []
        for i in range(len(player_names)):
            self.player_list.append(Player(player_names[i],self.dealerObj))   # creating the player list
        return None

    def play_rounds(self, num_rounds=1):
        """
        >>> import random; random.seed(1)
        >>> game = BlackjackGame(["Lawrence","Melissa"])
        >>> print(game.play_rounds(2))
        Round 1
        Dealer: [10, 9] 0/0/0
        Lawrence: [10, 6, 3] 0/1/0
        Melissa: [8, 8] 0/0/1
        Round 2
        Dealer: [10, 10] 0/0/0
        Lawrence: [10, 3] 0/1/1
        Melissa: [9, 10] 0/0/2
        """

        results = ""
        for i in range(num_rounds):
            results = results + "Round " + str(i+1) + '\n' #this will return Round number
            self.dealerObj.shuffle_deck()   #dealer shuffles the deck
            for player in self.player_list:  # gives one card to each player
                self.dealerObj.signal_hit(player)

            self.dealerObj.signal_hit(self.dealerObj)  #dealer gives a card to himself
            for player in self.player_list:
                self.dealerObj.signal_hit(player)   #deals the second card to all the players

            self.dealerObj.signal_hit(self.dealerObj)  #dealer gives a second card to himself
            for j in range(len(self.player_list)):
                self.player_list[j].play_round()    #If player wants to hit, giving them another card

            self.dealerObj.play_round()             #if dealer wants to hit, giving himself another card

            for j in range(len(self.player_list)):  #checking for wins, losses and ties 
                if self.dealerObj.card_sum >21:     #checking if dealer went bust
                    if self.player_list[j].card_sum >21:    # if player also went bust, player lost
                        self.player_list[j].record_loss()
                    else:
                        self.player_list[j].record_win()    # if player didnt go bust, player wins
                else:
                    if self.player_list[j].card_sum > 21:   # if player went bust and dealer didnt, player lost
                        self.player_list[j].record_loss()
                    elif self.dealerObj.card_sum < self.player_list[j].card_sum:  # comparing which sum is greater
                        self.player_list[j].record_win()
                    elif self.dealerObj.card_sum == self.player_list[j].card_sum:  # if equal , tie
                        self.player_list[j].record_tie()
                    else:
                        self.player_list[j].record_loss()

            results = results + repr(self.dealerObj) + '\n'   #Fromatting the results to show the updated record of wins,ties and losses

            for k in range(len(self.player_list)):
                if i == num_rounds-1:
                    if k == len(self.player_list)-1:
                        results = results + repr(self.player_list[k])
                    else:
                        results = results + repr(self.player_list[k]) + '\n'
                else:
                    results = results + repr(self.player_list[k]) + '\n'

            self.dealerObj.discard_hand()   #clearing out all the hands
            for x in range(len(self.player_list)):
                self.player_list[x].discard_hand()

        return results

    def reset_game(self):
        """
        >>> game = BlackjackGame(["Lawrence", "Melissa"])
        >>> _ = game.play_rounds()
        >>> game.reset_game()
        >>> game.player_list[0]
        Lawrence: [] 0/0/0
        >>> game.player_list[1]
        Melissa: [] 0/0/0
        """
        for i in range(len(self.player_list)):  #resting the stats and clearing the hands
            self.player_list[i].reset_stats()
            self.player_list[i].discard_hand()

        return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
