#write a program that simulates 1 round of Blackjack between two players

#initialize deck of cards --> class Deck
	#an instance of Deck should add 52 Card objects to an instance variable "cardList"
	#Deck should have a shuffle() method, which can be written by importing "random" into Python and and random.shuffle(myList) to shuffle 
	#a list of Card objects
import random  

#defines a "deck" of cards, initializes 52 cards and provides structure for dealing and shuffling
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

#defines card objects, assigns "value"
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

#defines a player class for player hands and hand values to be stored
class Player():
	def __init__(self):
		self.hand = []
		self.handTotal = 0  	
	def __repr__(self):
		return str(self.hand)

#initial showing of card for player and dealer		
def showHands(dealer, person):
	print("Dealer shows: " + str(dealer.hand[0]))
	print("You show: " + str(person.hand[0]))
	print(" ")

#unfinished code -- procedure for a turn. relies on all defined classes
def playersTurn(deck, person):
	print("You go first.")
	print(" ")
	
	print("You hold " + str(person.hand) + " for a total of " + str(person.handTotal))
	#ask the player if they'd like to hit or stay
	if (person.handTotal == 21):
		return "You won dude! Sick blackjack."
	else:
		if ["AH", "AS", "AC", "AD"] in person.hand:
			print("Assuming a value of 11 for Ace for right now.")
		decisionVar = int(input("Type 1 to hit or type 2 to stay: "))
		while (decisionVar == 1):
			deck.dealOne(person)
			if(person.handTotal < 21):
				print("You hold " + str(person.hand) + " for a total of " + str(person.handTotal))
				decisionVar = int(input("Type 1 to hit or type 2 to stay: "))
			elif(person.handTotal > 21):
				if ["AH", "AS", "AC", "AD"] in person.hand:
					print("You went over 21! Switching your Ace's 11 to a 1.")
					person.handTotal -= 10
				print("You hold " + str(person.hand) + " for a total of " + str(person.handTotal))
				decisionVar = int(input("Type 1 to hit or type 2 to stay: "))
				print("Bust!")
			else:
				print("21! Well, now it's my turn...")
				
def main():
	
	#initialize deck of cards and shuffle twice for good measure
	deckOfCards = Deck()
	deckOfCards.shuffle()
	deckOfCards.shuffle()
	
	#initialize dealer and player
	dealer = Player()
	person = Player()
	
	#start the round
	deckOfCards.dealOne(person)
	deckOfCards.dealOne(dealer)
	deckOfCards.dealOne(person)
	deckOfCards.dealOne(dealer)
	
	#the big reveal
	showHands(dealer,person)
	
	#play begins in earnest
	playersTurn(deckOfCards, person)
	
main()