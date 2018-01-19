## blackjack implementation
## single player and dealer game
import tkinter
import random


def load_images(card_images):
    suits = ["heart", "club", "diamond", "spade"]
    face_card = ["jack", "queen", "king"]
    # each suit and card fatch image
    for suit in suits:
        # first fatch.1 to 10
        for card in range(1, 11):
            name = 'cards/{}_{}.ppm'.format(card, suit)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))
        # next the face cards
        for card in face_card:
            name = "cards/{}_{}.ppm".format(card, suit)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


def deal_card(frame):
    # pop the next card from the deck pop the card thats on top of the dack
    next_card = deck.pop(0)
    # add back at pack
    deck.append(next_card)
    # add the imgage to label and display the label
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
    # Usually we use grid and frames but here we are stacking cards on each other
    # so its better to use pack then grid as we can add ea
    ## now return the card's face value
    return next_card

def score_hand(hand):
    # calculate total score for a hand passed to it
    # only one ace can have value 11 and this will be reduced to 1 if hand is about to bust
    score = 0
    ace=  False
    for nxt_card in hand:
        card_value = nxt_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if we would bust, check if there is an ace and substract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand((player_hand))
    player_score_label.set(player_score)
    if(player_score > 21):
        result_Text.set("Dealer wins!")


def deal_dealer():
    dealer_score =score_hand((dealer_hand))
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand((dealer_hand))
        dealer_score_label.set(dealer_score)

    player_score = score_hand((player_hand))
    # check who as won game
    if(player_score > 21):
        result_Text.set("Dealer wins!")
    elif(dealer_score > 21 and dealer_score < player_score):
        result_Text.set("Player wins!")
    elif(dealer_score > player_score):
        result_Text.set("Dealer wins!")
    else :
        result_Text.set("Draw..!")

def init():
    deal_player()
    dealer_hand.append((deal_card(dealer_card_frame)))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    ## embeddd card frame to hold card images
    dealer_card_frame.destroy()
    dealer_card_frame =  tkinter.Frame(card_frame,background="grey")
    dealer_card_frame.grid(row=0,column=1,sticky="ew", rowspan=2)
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="grey")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    result_Text.set("")
    ## create the list to dealer's and player's hand
    dealer_hand = []
    player_hand = []
    init()


def shuffle():
    random.shuffle(deck)

def play():
    init()
    mainWindow.mainloop()


if(__name__ == '__main__'):
    ##setup the screen and frames for d wgsealer and player
    mainWindow = tkinter.Tk()
    mainWindow.title("BlackJack")
    mainWindow.geometry("640x480")
    mainWindow.configure(background="grey")

    result_Text = tkinter.StringVar()
    result = tkinter.Label(mainWindow, textvariable=result_Text,background="grey",fg="white")
    result.grid(row=0, column=0, columnspan=3)
    card_frame = tkinter.Frame(mainWindow, relief="sunken", background="grey")
    card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

    dealer_score_label = tkinter.IntVar()
    tkinter.Label(card_frame, text="Dealer", background="grey", fg="white").grid(row=0, column=0)
    tkinter.Label(card_frame, textvariable=dealer_score_label, background="grey", fg="white").grid(row=1, column=0)
    ## Embedded frame hold the card images
    dealer_card_frame = tkinter.Frame(card_frame, background="grey")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    ##player frames
    player_score_label = tkinter.IntVar()
    player_score = 0
    player_ace = False

    tkinter.Label(card_frame, text="Player", background="grey", fg="white").grid(row=2, column=0)
    tkinter.Label(card_frame, textvariable=player_score_label, background="grey", fg="white").grid(row=3, column=0)

    ##embedded frame for player cards
    player_card_frame = tkinter.Frame(card_frame, background="grey")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    button_frame = tkinter.Frame(mainWindow,background="grey")
    button_frame.grid(row=3, column=0, sticky="ew")

    dealer_button = tkinter.Button(button_frame, text="Dealer", background="grey", command=deal_dealer)
    dealer_button.grid(row=0, column=1)

    player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
    player_button.grid(row=0, column=2)

    new_game_button= tkinter.Button(button_frame,text="New Game", command=new_game)
    new_game_button.grid(row=1, column=1)

    shuffle_button= tkinter.Button(button_frame,text="Shuffle", command=shuffle)
    shuffle_button.grid(row=1, column=2)
    # load card
    cards = []
    load_images(cards)

    ## create the list to dealer's and player's hand
    dealer_hand = []
    player_hand = []

    ##create new deck of cards and shuffle them
    deck = list(cards)
    shuffle()

    play()
    ## append and pop used to handle cards in deck to get and add card