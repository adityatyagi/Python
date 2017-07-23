try:
    import tkinter
except ImportError:
    import Tkinter as tkinter



import random


# Load Card Images
def load_images(card_images):

    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    # extention of all the card images to be laoded is .png
    extention = 'png'

    # for each suit, retrieve the image for the cards
    for suit in suits:
        # retreive the number cards - 1 to 10
        for card in range(1, 11):
            name = 'BlackJack\\cards\\{}_{}.{}'.format(str(card), suit, extention) # extracting name of the image file
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))
        
        # retrieve the face cards
        for card in face_cards:
            name = 'BlackJack\\cards\\{}_{}.{}'.format(str(card), suit, extention) # extracting name of the image file
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))
            


def deal_card(frame):
    # pop the next card from top of the deck
    next_card = deck.pop(0)

    # add image to a label and display the label
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")

    # return the cards face value -> that is the number on the card
    return next_card



def score_hand(hand):
    # calculate the total score of the hand at one place, rather than calculating it seprately
    # Only one ace can have value 11, and if we bust, the value of ace become 1
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value

        # if we would bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False

    return score



def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
    

    player_score = score_hand(player_hand)

    if player_score > 21:
        result_text.set("Dealer Wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
    else:
        result_text.set("Draw")


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")


def newgame():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand

    # dealer frame to hold the card images
    # BUT FRIST DESTROY THE DEALER CARD FRAME
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="pink")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    # player frame to hold the card images
    player_card_frame = tkinter.Frame(card_frame, background="red")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    # reset the result_text
    result_text.set("")

    # Create new empty list to hold the dealer and player's hands
    dealer_hand = []
    player_hand = []

    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()



def shuffle():
    random.shuffle(deck)



mainWindow = tkinter.Tk()
mainWindow.title("Blackjack Game")
mainWindow.geometry('400x280')
mainWindow["padx"] = 10



result_text = tkinter.StringVar() # .SrtingVar() makes result_text a value holder for string values
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

# Frame to hold the cards
card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)


# Dealer Card Frame - Frame to hold the dealer's cards
dealer_card_frame = tkinter.Frame(card_frame, background="pink")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2) # row and column values are respective to the card_frame

# Player Card Frame - - Frame to hold the player's cards 
player_card_frame = tkinter.Frame(card_frame, background="red")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

# Dealer Score Label
dealer_score_label = tkinter.IntVar() # .IntVar() makes dealer_score_label a value holder for int values

# Label for the word "DEALER"
tkinter.Label(card_frame, text="DEALER", background="pink", fg="black").grid(row=0, column=0)
# Label for dealer's score
tkinter.Label(card_frame, textvariable=dealer_score_label, background="pink", fg="black").grid(row=1, column=0)




# Player Score Label
player_score_label = tkinter.IntVar() # .IntVar() makes dealer_score_label a value holder for int values

player_score = 0
player_ace = False

# Label for the word "PLAYER"
tkinter.Label(card_frame, text="PLAYER", background="red", fg="white").grid(row=2, column=0)

# Label for player's score
tkinter.Label(card_frame, textvariable=player_score_label, background="red", fg="white").grid(row=3, column=0)


# ----------- Buttons - Dealer, Player, New Game, Shuffle ---------------

# Frame to hold the buttons
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky="ns")
button_frame["pady"]=10

# Dealer Button
dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer) # and not command=deal_dealer()
dealer_button.grid(row=0, column=0)

# Player Button
player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

# Shuffle Button
shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=2)

# New Game Button
newgame_button = tkinter.Button(button_frame, text="New game", command=newgame)
newgame_button.grid(row=0, column=3)



# Load Cards
cards = []
load_images(cards)
print(cards)

# Create a new deck of cards and Shuffle the cards using thr random module
deck = list(cards) + list(cards) + list(cards)
shuffle()


# Create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []


newgame()

mainWindow.mainloop()