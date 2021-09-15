import random
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
mainWindow = tkinter.Tk()

def load_images(card_images):
    suits=['heart','club','diamond','spade']
    face_cards=['jack','queen','king']

    if tkinter.TkVersion >=8.6:
        extension='png'
    else:
        extension='ppm'
    #for each suit retrive each image for the cards
    for suit in suits:
        #first the number of cards from 1to 10
        for card in range(1,11):
            name='cards/{}_{}.{}'.format(str(card),suit,extension)
            image=tkinter.PhotoImage(file=name) #mention the name of the file. you can download images,online.
            card_image.append((card,image))
        #next the face cards
        for card in face_cards:
            name='cards/{}_{}.{}'.format(str(card),suit,extension)
            image=tkinter.PhotoImage(file=name)
            card_image.append((10,image))
        
def deal_card(frame):
    #pop the next card off the top of the deck
    next_card=deck.pop()
    #add the image to lable and display the lable
    tkinter.Label(frame,image=next_card[1],relief='raised').pack(side="left")
    #now return the cards face value
    return next_card
def deal_dealer():
    deal_card(dealer_card_frame)

def deal_player():
    deal_card(player_card_frame)
    
# set up the screen for the dealer and player
mainWindow.title("Black jack")
mainWindow.geometry("640x480")

result_text = tkinter.StringVar()
result= tkinter.Label(mainWindow,textvariable= result_text)

card_Frame = tkinter.Frame(mainWindow, relief='sunken',borderwidth=1,background="green")
card_Frame.grid(row=1,column=1,sticky='ew', columnspan=3, rowspan=2)

dealer_score_lable= tkinter.IntVar()
tkinter.Label(card_Frame, text="Dealer",background="green", fg='white').grid(row=0,column=0)
tkinter.Label(card_Frame, textvariable = dealer_score_lable,background='green',fg='white').grid(row=1,column=0)
#embbeded frame hold the card images
dealer_card_frame= tkinter.Frame(card_Frame,background="green")
dealer_card_frame.grid(row=0,column=1,sticky='ew',rowspan=2)

player_score_lable = tkinter.IntVar()
tkinter.Label(card_Frame, text="Player",background='green', fg='white').grid(row=2,column=0)
tkinter.Label(card_Frame, textvariable=player_score_lable,background='green',fg='white').grid(row=3,column=0)

#embbeded frame to hold the card images
player_card_frame= tkinter.Frame(card_Frame,background="green",)
player_card_frame.grid(row=2,column=1,sticky='ew',rowspan=2)

button_frame= tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0,columnspan=3,sticky='w')

dealer_button= tkinter.Button(button_frame,text="Dealer",command=deal_dealer)
dealer_button.grid(row=0,column=0)

player_button = tkinter.Button(button_frame, text="Player",command=deal_player)
player_button.grid(row=0,column=1)

cards=[]
load_images(cards)
print(cards)
#create a new deck of cards and shuffle them
deck = list(cards)
random.shuffle(deck)
#create the list to store the dealers and players hand
dealer_hand=[]
player_hand=[]
mainWindow.mainloop()
