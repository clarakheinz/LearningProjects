import random
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9,'Ten':10, 'Jack':10,'Queen':10,'King':10, 'Ace':0}
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal(self):
        return self.all_cards.pop()

class Player:
    def __init__(self):
        self.all_cards = []
        self.values = 0
        self.aces = 0

        
    def add_card(self, newcard):
        self.all_cards.append(newcard)
        self.values += newcard.value
        
        if newcard.rank == 'Ace':
            left = 21 - self.values
            if left >= 11:
                self.values += 11
            else:
                self.values += 1
    

        
    def __str__(self):
        return f"Player hand: {len(self.all_cards)} cards."

class Dealer:
    def __init__(self):
        self.all_cards = []
        self.values = 0
        self.aces = 0


    def add_card(self, newcard):
        self.all_cards.append(newcard)
        self.values += newcard.value

        if newcard.rank == 'Ace':
            left = 21 - self.values
            if left >= 11:
                self.values += 11
            else:
                self.values += 1

    def __str__(self):
        return f'Dealer hand: {len(self.all_cards)} cards.'

class Chips:
    def __init__(self):
        self.total_money = 1000

    def __str__(self):
        return f'You have: {self.total_money} in chips.'

    def win_bet(self, amount):
        self.total_money += amount

    def lose_bet(self, amount):
        self.total_money -= amount

def hit(deck, player):
    player.add_card(deck.deal())

def hit_stand(deck, player):
    global playing
    answer = input("Hit or Stand? ")
    while answer not in ['Hit','Stand']:
        answer = input("I/'m sorry. I did not catch that. Hit or stand? ")
    if answer == "Hit":
        hit(deck, player)
    elif answer == "Stand":
        playing=False



def show_some(player, dealer):
    print("Player's hand: ")
    for card in player.all_cards:
        print(card)
    print(f'Hand value: {player.values}')
    print("\nDealer's hand: ")
    print('<card hidden>')
    for card in dealer.all_cards[1:]:
        print(card)
    print('\n')

def show_all(player, dealer):
    print("Player's hand: ")
    for card in player.all_cards:
        print(card)
    print(f'Hand value: {player.values}')
    print("\nDealer's hand: ")
    for card in dealer.all_cards:
        print(card)
    print(f'Dealer hand value: {dealer.values}\n')

def player_wins(player, dealer, player_chips,bet):
    show_all(player,dealer)
    print("Player wins!")
    player_chips.win_bet(bet)
def dealer_wins(player, dealer, player_chips,bet):
    show_all(player, dealer)
    print("Dealer wins!")
    player_chips.lose_bet(bet)
def player_busts(player,dealer, player_chips,bet):
    show_all(player, dealer)
    print("Player busts!")
    player_chips.lose_bet(bet)
def dealer_busts(player, dealer, player_chips,bet):
    show_all(player,dealer)
    print("Dealer busts!")
    player_chips.win_bet(bet)

def main():
    global playing
    playing =True
    while True:
        print("Welcome to BlackJack!")
        read_rules = input("Do you need to read the rules? (Y/N) ")
        while read_rules not in ['Y','N']:
            print("I'm sorry, please try again.")
            read_rules = input("Do you need to read the rules? (Y/N) ")
        if read_rules == 'Y':
            print("BlackJack is a fun casino game where it's just you against the Dealer. The goal is to get as close to 21 with the value of your cards without going over. Jack, Queen, King are valued at 10, Ace can be 1 or 11 (but don't worry, the computer will figure out which it should be), and numerical cards are the value of their rank. You will be asked how much you want to bet, then the cards will be dealt. You will receive 2 face up, and the Dealer will receive 1 face down and another face up. You will get the chance to Hit or Stand. Hit will add a card to your hand, stand will end your turn. The Dealer will then Hit until they reach 17 or bust. You must beat the Dealer to win your bet. Good luck!")
        # Game setup
        player = Player()
        new_deck = Deck()
        new_deck.shuffle()
        dealer = Dealer()
    
        player.add_card(new_deck.deal())
        player.add_card(new_deck.deal())
        dealer.add_card(new_deck.deal())
        dealer.add_card(new_deck.deal())

        player_chips = Chips()
        if player_chips.total_money == 0:
            print("You have no money! Game over!")
            break

        while True:
            try:
                bet = int(input("How much would you like to bet? Please enter a number. "))
            except:
                print("Please try again. Input a number. ")
            else:
                if bet >= player_chips.total_money:
                    print(f"I'm sorry, you only have {player_chips.total_money}.")
                else:
                    break
    
        show_some(player, dealer)

        while playing:
            hit_stand(new_deck, player)
            show_some(player, dealer)
    
            if player.values > 21:
                player_busts(player, dealer, player_chips, bet)
                break
    
        if player.values <= 21:
            print("Dealer's turn.")
            while dealer.values < 17:
                dealer.add_card(new_deck.deal())
                show_some(player, dealer)
    
            if dealer.values > 21:
                dealer_busts(player, dealer, player_chips,bet)
    
            elif (dealer.values < 21) & (21 - dealer.values < 21 - player.values):
                dealer_wins(player, dealer, player_chips,bet)
            else:
                player_wins(player, dealer, player_chips,bet)
        print(f'You have {player_chips.total_money} chips.')
        play_again = input("Would you like to play again? Y/N ")
        while play_again not in ['Y','N']:
            print("I am sorry, I did not catch that.")
            play_again = input("Would you like to play again? Y/N ")
        if play_again == 'Y':
            playing=True
        else:
            print("Thanks for playing BlackJack!")
            break

if __name__ == "__main__":
    main()
