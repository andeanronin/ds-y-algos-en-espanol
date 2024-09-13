import random

# Card Game:
# 1. Ask player names and set them
# 2. Get 2 cards from a deck of cards
# 3. Add 1 card to each player's hand
# 4. Compare cards by number. If equal, by 
# 5. Person with larger card removes card from their hand, 
# 6. Player with smaller card adds card to their hand
# 7. When deck is empty, compare the number of cards players have. Player with less cards wins. 

# Two classes: player & card deck
class Player(object):
    "A player class, with attributes: name, hand"
    def __init__(self, name):
        "Sets attributes hand (list) and name (string)"
        self.hand = []
        self.name = name 
    
    def get_name(self):
        "Returns name of the player"
        return self.name
    
    def add_card_to_hand(self, card):
        if card != None:
            self.hand.append(card)

    def remove_card_from_hand(self, card):
        self.hand.remove(card) 

    def hand_size(self):
        "returns length of player's hand"
        return len(self.hand)
    
    

class CardDeck(object):
    def __init__(self):
        hearts = "2H,3H,4H,5H,6H,7H,8H,9H"
        diamonds = "2D,3D,4D,5D,6D,7D,8D,9D"
        spades = "2S,3S,4S,5S,6S,7S,8S,9S"
        clubs = "2C,3C,4C,5C,6C,7C,8C,9C"
        self.deck = hearts.split(',') + diamonds.split(',')  + spades.split(',')+clubs.split(',')
    
    def get_card(self):
        if len(self.deck) < 1:
            return None
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card 
    
    def compare_cards(self, card1, card2):
        if card1[0] > card2[0]:
            return card1
        if card1[0] < card2[0]:
            return card2
        
        elif card1[1] > card2[1]:
            return card1
        
        else: 
            return card2
        

if __name__ == "__main__":
    # 1. get name from player 1
    name1 = input("Whats your name? Player 1: ")
    # 1.1 initialize player 1 object with name gotten from player
    player1 = Player(name1)
    # 2. get name from player 2
    name2 = input("Whats your name? Player 2: ")
    # 2.1 initialize player 2 object with name gotten from player
    player2 = Player(name2)

    # 3. create card deck
    deck = CardDeck()


    # 4. Start the game:
    while True:
        # Get cards from deck and assign them to each player
        player1card = deck.get_card()
            # if there are cards in deck, a card is assigned to player1card
            # but if there are no more cards in deck player1card = None
        player2card = deck.get_card()

        # Add those cards to each player's hands:
        player1.add_card_to_hand(player1card)
        player2.add_card_to_hand(player2card)

        # If there are no more cards in deck (ie., player1card or player2 cards are None)
        # Compare size of player's hands
        if player1card == None or player2card == None:
            print("Game Over. No more cards in deck")
            print(f"{player1.name} has {player1.hand_size()}")
            print(f"{player2.name} has {player2.hand_size()}")
            print("Who won?")
            # Compare how big each players hands are, player with less cards wins
            if player1.hand_size() > player2.hand_size():
                print(f"{player1.name} won")
            elif player1.hand_size() < player2.hand_size():
                print(f"{name2} won")
            else: 
                print("A Tie!")
            break

        # If there are cards in deck, compare each player's cards 
        # Remove card from player with largest card hand's
        # Add card to the hand of the player with the smaller card
        else:
            print(name1, ": ", player1card)
            print(name2, ":", player2card)
            if deck.compare_cards(player1card, player2card) == player1card:
                player1.remove_card_from_hand(player1card)
                player2.add_card_to_hand(player1card)
            else:
                player2.remove_card_from_hand(player2card)
                player1.add_card_to_hand(player2card)