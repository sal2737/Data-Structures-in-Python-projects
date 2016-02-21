#write a program that simulates 1 round of Blackjack between two players

#initialize deck of cards --> class Deck
	#an instance of Deck should add 52 Card objects to an instance variable "cardList"
	#Deck should have a shuffle() method, which can be written by importing "random" into Python and and random.shuffle(myList) to shuffle 
	#a list of Card objects
import random  
class Deck():
    def __init__(self):
        self.cardList = []
        #class variables for Deck -- can be based on paramters passed to the __init__ method
    	#it should add 52 Card objects to an instance variable "cardList".
        for suit in ["C", "D", "H", "S"]:
            for pip in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
            	#cardObject = Card(suit, pip)
            	self.cardList.append(Card(suit, pip))
        		
    def shuffle(self):
        random.shuffle(self.cardList)
    def dealOne(self, player):
    	player.handTotal += self.cardList[0].value #numerical value of card
    	player.hand.append(self.cardList[0])
    	self.cardList.pop(0)
	
    def __repr__(self):
        return (self.cardList) #add str for the test case, to print out

#card objects
class Card(Deck):
    def __init__(self, suit, pip):
        self.suit = suit
        self.pip = pip
        if(self.pip == "J" or self.pip == "Q" or self.pip == "K"):
        	self.value = 10
        elif(pip == "A"):
        	self.value = 11
        else:
        	self.value = int(pip)
    def __repr__(self):
    	return self.pip + self.suit

class Player():
	def __init__(self):
		self.hand = []
		self.handTotal = 0  	
	def __repr__(self):
		return self.hand 
		
def main():
	
	#initialize deck of cards
	deckOfCards = Deck()
	
	#initialize player and dealer
	dealer = Player()
	person = Player()
	
	#start the round
	deckOfCards.dealOne(person)
	deckOfCards.dealOne(dealer)
	deckOfCards.dealOne(person)
	deckOfCards.dealOne(dealer)
	print(str(dealer))
	print(str(person))
main()
#deal 2 cards to each player (dealer/computer and user)

#an ace with any 10-pt card is a blackjack. if both the dealer and player draw blackjack, the tie goes to the dealer.

#player always goes first

#The player can choose to keep his/her hand as it is ("stand" or "stay") or request more cards from the deck ("hit"), one at a time
#while loop would be good
#If the dealer's hand is still lower than the player's hand, the dealer draws another card.
