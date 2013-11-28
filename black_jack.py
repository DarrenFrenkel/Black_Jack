# Mini-project #6 - Blackjack

import simpleguitk as simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
deck = []
players_hand = []
dealers_hand = []
pozish = [0,0]
pozishd = [0,0]
outcome = ""


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print ("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        ans = ''
        for i in range(len(self.cards)):
            ans += str(self.cards[i]) + " "
        return "Hand contains " + ans
 
        pass	# return a string representation of a hand

    def add_card(self, card):
        self.cards.append(card)


    def get_value(self):
        ranks = ""
        total_value = 0
        none_value = 0
        
        for i in self.cards:
            ranks += i.get_rank()
        
        for i in ranks:
           total_value += VALUES[i]
       
        for i in ranks:
           if i != 'A':
                return total_value
           elif i == 'A':
                if total_value + 10 >=21:
                    return total_value
                else:
                    return total_value + 10
        return total_value  
   

        self.canvas = canvas
        self.pos = pos
        x.draw(canvas,pos)
      
        
# define deck class 
class Deck:
    def __init__(self):
        pass	# create a Deck object
        self.card_deck = []
        for suits in SUITS:
            for ranks in RANKS:
                card = Card(suits,ranks)
                self.card_deck.append(card)
        

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.card_deck)
        pass    # use random.shuffle()

    def deal_card(self):
        pass	# deal a card object from the deck
        card = self.card_deck[-1]
        self.card_deck.pop()
        return card
        
    def __str__(self):
        pass	# return a string representing the deck
        ans = ''
        for i in range(len(self.card_deck)):
            ans += str(self.card_deck[i]) + " "
        return "Deck contains " + ans

            
        


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, players_hand, dealers_hand, pozish
    outcome = "hit or stand?"
    deck = Deck()
    deck.shuffle()
   
    
    players_hand = Hand()
    dealers_hand = Hand()
    players_hand.add_card(deck.deal_card())
    dealers_hand.add_card(deck.deal_card())
    players_hand.add_card(deck.deal_card())
    dealers_hand.add_card(deck.deal_card())
    
    in_play = True

def hit():
    global players_hand, outcome, in_play
    if players_hand.get_value() <= 21:
        players_hand.add_card(deck.deal_card())
        
        if players_hand.get_value() > 21:
            outcome = "You Have Busted, New Deal"
            in_play = False
        
   
        
        
    pass	# replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, in_play
    if players_hand.get_value() > 21:
        outcome = "You Have Busted, New Deal?"
        in_play = False
    elif players_hand.get_value() <= 21:
        while dealers_hand.get_value() < 17:
            dealers_hand.add_card(deck.deal_card())
  
        if dealers_hand.get_value() > 21:
            outcome = "You Win!!!, New Deal?"
            in_play = False
        else: 
            if dealers_hand.get_value() >= players_hand.get_value():
                outcome = "Win goes to the dealer, New Deal?"
                in_play = False
            else:
                outcome = "You Win!!!, New Deal?"
                in_play = False
    else:
        outcome = "hit or stand?"

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    pozish[0] = 20
    pozish[1] = 90
    for x in players_hand.cards:
        x.draw(canvas, pozish)
        pozish[0] += 83
        
    pozishd[0] = 20
    pozishd[1] = 350
    for x in dealers_hand.cards:
        x.draw(canvas, pozishd)
        pozishd[0] += 83
        
    if in_play == True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (58,400), CARD_SIZE)
        
    canvas.draw_text(outcome, (25,280), 40, "White")
    canvas.draw_text("Black Jack", (220,35), 40, "Black")
    canvas.draw_text("Player", (30,80), 20, "Red")
    canvas.draw_text("Dealer", (30,340), 20, "Red")


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric