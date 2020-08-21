from tkinter import *
#Moves has diferent numbers so de if else conditions doesnt enter like what would happens if the where just blank spaces



# ___________________________________________________________________
#|                                                                   |
#|                     Functions                                     |
#|___________________________________________________________________|

#------------Control buttons functions-----------------------------------
def changetomenu2():
    
    global rounds_wonG1
    global rounds_wonG2
    
    #Clean menu1 windows labels
    label_tic.place_forget()
    label_tac.place_forget()
    label_toe.place_forget()
    start_button.place_forget()
    
    #Clean win windows
    label_win.place_forget()
    label_scores.place_forget()
    label_win_name.place_forget()
    label_win1.place_forget()
    label_win1pts.place_forget()
    label_win2.place_forget()
    label_win2pts.place_forget()
    different_players_button.place_forget()
    new_game_button.place_forget()
    #Clean table labels
    label_00.place_forget()
    label_01.place_forget()
    label_02.place_forget()
    label_10.place_forget()
    label_11.place_forget()
    label_12.place_forget()
    label_20.place_forget()
    label_21.place_forget()
    label_22.place_forget()
    #place board buttons
    button_00.place_configure(x=349, y=70 )
    button_01.place_configure(x=430, y=70 )
    button_02.place_configure(x=518, y=70 )
    button_10.place_configure(x=349, y=150)
    button_11.place_configure(x=430, y=150)
    button_12.place_configure(x=518, y=150)
    button_20.place_configure(x=349, y=230)
    button_21.place_configure(x=430, y=230)
    button_22.place_configure(x=518, y=230)
    
    #place menu2 windows labels
    label_player1.place_configure(x=38, y=50)
    text_player1.place_configure(x=40, y=100)
    label_x.place_configure(x=200, y=30)
    label_player2.place_configure(x=38, y=150)
    text_player2.place_configure(x=40, y=200)
    label_o.place_configure(x=200, y=125)
    ready_button.place_configure(x=130, y=270)
    
    rounds_wonG1 = 0
    rounds_wonG2 = 0
    
def changetomenu3():
    
    global game_start
    
    if text_player1.get() != "" and text_player2.get() != "":
        #Clean menu2 windows
        label_player1.place_forget()
        text_player1.place_forget()
        label_x.place_forget()
        label_player2.place_forget()
        text_player2.place_forget()
        label_o.place_forget()
        ready_button.place_forget()
        #Clean win windows
        label_win.place_forget()
        label_scores.place_forget()
        label_win_name.place_forget()
        label_win1.place_forget()
        label_win1pts.place_forget()
        label_win2.place_forget()
        label_win2pts.place_forget()
        different_players_button.place_forget()
        new_game_button.place_forget()
        #Clean table labels
        label_00.place_forget()
        label_01.place_forget()
        label_02.place_forget()
        label_10.place_forget()
        label_11.place_forget()
        label_12.place_forget()
        label_20.place_forget()
        label_21.place_forget()
        label_22.place_forget()
        
        #place board buttons
        button_00.place_configure(x=349, y=70)
        button_01.place_configure(x=430, y=70)
        button_02.place_configure(x=518, y=70)
        button_10.place_configure(x=349, y=150)
        button_11.place_configure(x=430, y=150)
        button_12.place_configure(x=518, y=150)
        button_20.place_configure(x=349, y=230)
        button_21.place_configure(x=430, y=230)
        button_22.place_configure(x=518, y=230)
        #place rest labels
        label_turn.place_configure(x=38, y=50)
        
        label_big.place_configure(x=100, y=180)
        label_guide.place_configure(x=38, y=300)
        if turn_count == True:#set the name becouse the player who start changes every match.
            m3label_player.place_configure(x=38, y=150)
            m3label_player.config(text=text_player1.get())
        else:
            m3label_player.place_configure(x=38, y=150)
            m3label_player.config(text=text_player2.get())
        game_start = 1
        
def changeplayer():
    """this function changes the name and the mark indicating if is used x or 0"""
    if turn_count == True:
        m3label_player.config(text=text_player1.get(), justify="center")
        label_big.config(text=label_x.cget("text"))
    else:
        m3label_player.config(text=text_player2.get(), justify="center")
        label_big.config(text=label_o.cget("text"))
    
#|-------------------------------------------------------------------------------------|        
#|                             Game buttons functions                                  |
#|-------------------------------------------------------------------------------------|

def game_button_pressed(val):
    
    global turn_count
    global moves
    
    # I use turn_count to change the number and de letter in the menu3 and then the
    #  changeplayer function to change those values
    
    
    if game_start == 1:
        if val == "7":
            button_00.place_forget()
            label_00.place_configure(x=363, y=70, height = 68)
            label_00.config(text=label_big.cget("text"))
            turn_count = not turn_count
            moves["7"] = label_big.cget("text")
            changeplayer()
            checkmatch()
        elif val == "8":
            button_01.place_forget()
            label_01.place_configure(x=447, y=70, height = 68)
            label_01.config(text=label_big.cget("text"))
            turn_count = not turn_count
            moves["8"] = label_big.cget("text")
            changeplayer()
            checkmatch()
        elif val == "9":
            button_02.place_forget()
            label_02.place_configure(x=530, y=70, height = 68)
            label_02.config(text=label_big.cget("text"))
            turn_count = not turn_count
            moves["9"] = label_big.cget("text")
            changeplayer()
            checkmatch()
        elif val == "4":
            button_10.place_forget()
            label_10.place_configure(x=363, y=150, height = 68)
            label_10.config(text=label_big.cget("text"))
            turn_count = not turn_count
            moves["4"] = label_big.cget("text")
            changeplayer()
            checkmatch()
        elif val == "5":
            button_11.place_forget()
            label_11.place_configure(x=447, y=150, height = 68)
            label_11.config(text=label_big.cget("text"))
            turn_count = not turn_count
            moves["5"] = label_big.cget("text")
            changeplayer()
            checkmatch()
        elif val == "6":
            button_12.place_forget()
            label_12.place_configure(x=530, y=150, height = 68)
            label_12.config(text=label_big.cget("text"))
            turn_count = not turn_count
            moves["6"] = label_big.cget("text")
            changeplayer()
            checkmatch()
        elif val == "1":
            button_20.place_forget()
            label_20.place_configure(x=363, y=230, height = 68)
            label_20.config(text=label_big.cget("text"))
            turn_count = not turn_count
            moves["1"] = label_big.cget("text")
            changeplayer()
            checkmatch()
        elif val == "2":
            button_21.place_forget()
            label_21.place_configure(x=447, y=230, height = 68)
            label_21.config(text=label_big.cget("text"))
            turn_count = not turn_count
            moves["2"] = label_big.cget("text")
            changeplayer()
            checkmatch()
        elif val == "3":
            button_22.place_forget()
            label_22.place_configure(x=530, y=230, height = 68)
            label_22.config(text=label_big.cget("text"))
            turn_count = not turn_count
            moves["3"] = label_big.cget("text")
            changeplayer()
            checkmatch()
            
            
        
            
        
def youwin():
    
    global game_start
    
    # Clean table labels
    label_00.place_forget()
    label_01.place_forget()
    label_01.place_forget()    
    label_10.place_forget()
    label_11.place_forget()
    label_12.place_forget()    
    label_20.place_forget()
    label_21.place_forget()
    label_22.place_forget()
    #Clean menu3 windows labels
    label_turn.place_forget()
    m3label_player.place_forget()
    label_big.place_forget()
    label_guide.place_forget()
    
    
    label_win.place_configure(x=330, y=60)#Picture Well Done
    label_win.config(image=image_win)
    label_win_name.place_configure(x=330, y=250, relwidth=0.5)# Name of the winner under picture
    label_win_name.config(text=winner)
    label_scores.place_configure(x=70, y=40)
    label_win1.place_configure(x=30, y=120)
    label_win1.config(text=text_player1.get())
    label_win1pts.place_configure(x=200, y=120)
    label_win1pts.config(text=rounds_wonG1)
    label_win2.place_configure(x=30, y=190)
    label_win2.config(text=text_player2.get())
    label_win2pts.place_configure(x=200, y=190)
    label_win2pts.config(text=rounds_wonG2)
    different_players_button.place_configure(x=30, y=270)
    new_game_button.place(x=170, y=270)
    
    game_start = 0
    
def istie():
    
    global game_start
    global moves
    global moves_count
    
    # Clean table labels
    label_00.place_forget()
    label_01.place_forget()
    label_01.place_forget()    
    label_10.place_forget()
    label_11.place_forget()
    label_12.place_forget()    
    label_20.place_forget()
    label_21.place_forget()
    label_22.place_forget()
    #Clean menu3 windows labels
    label_turn.place_forget()
    m3label_player.place_forget()
    label_big.place_forget()
    label_guide.place_forget()
    
    
    label_win.place_configure(x=330, y=60)#Picture Well Done
    label_win.config(image=image_tie)
    label_win_name.place_configure(x=330, y=250, relwidth=0.5)# Black empty Label to hice the 2 bars showing under the picture
    label_win_name.config(text="")
    label_scores.place_configure(x=70, y=40)
    label_win1.place_configure(x=30, y=120)
    label_win1.config(text=text_player1.get())
    label_win1pts.place_configure(x=200, y=120)
    label_win1pts.config(text=rounds_wonG1)
    label_win2.place_configure(x=30, y=190)
    label_win2.config(text=text_player2.get())
    label_win2pts.place_configure(x=200, y=190)
    label_win2pts.config(text=rounds_wonG2)
    different_players_button.place_configure(x=30, y=270)
    new_game_button.place(x=170, y=270)
    
    moves = {"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}#to reset the 
    #evaluators so the game doesnt remember pressed buttons from the previous game
    game_start = 0
    moves_count = 0
    




#---------------Game logic functions----------------------------------------------------

def checkwinner():
# Check every time a button is pressed if there is a winner.
    
    global rounds_wonG1
    global rounds_wonG2
    global winner
    global moves
    global moves_count
            
    if moves["1"] == moves["2"] and moves["1"] == moves["3"]:
        
        if moves["1"] == gamer1:
            winner = text_player1.get()
            
            rounds_wonG1 += 1
                  
        else:
            winner = text_player2.get()
            rounds_wonG2 += 1
        youwin()
        moves = {"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}#to reset the 
        #evaluators so the game doesnt remember pressed buttons from the previous game
        moves_count = -1
    elif moves["4"] == moves["5"] and moves["4"] == moves["6"]:
        
        if moves["4"] == gamer1:
            winner = text_player1.get()
            
            rounds_wonG1 += 1
                   
        else:
            winner = text_player2.get()
            rounds_wonG2 += 1
        youwin()
        moves = {"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}#to reset the 
        #evaluators so the game doesnt remember pressed buttons from the previous game
        moves_count = -1
    elif moves["7"] == moves["8"]and moves["7"] == moves["9"]:
        
        if moves["7"] == gamer1:
            winner = text_player1.get()
            
            rounds_wonG1 += 1
            
        else:
            winner = text_player2.get()
            rounds_wonG2 += 1
        youwin()
        moves = {"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}#to reset the 
        #evaluators so the game doesnt remember pressed buttons from the previous game
        moves_count = -1
    elif moves["1"] == moves["4"]and moves["1"] == moves["7"]:
        
        if moves["1"] == gamer1:
            winner = text_player1.get()
            
            rounds_wonG1 += 1
            
        else:
            winner = text_player2.get()
            rounds_wonG2 += 1
        youwin()
        moves = {"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}#to reset the 
        #evaluators so the game doesnt remember pressed buttons from the previous game
        moves_count = -1
    elif moves["2"] == moves["5"] and moves["2"] == moves["8"]:
        
        if moves["2"] == gamer1:
            winner = text_player1.get()
            
            rounds_wonG1 += 1
            
        else:
            winner = text_player2.get()
            rounds_wonG2 += 1
        youwin()
        moves = {"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}#to reset the 
        #evaluators so the game doesnt remember pressed buttons from the previous game
        moves_count = -1
    elif moves["3"] == moves["6"] and moves["3"] == moves["9"]:
        
        if moves["3"] == gamer1:
            winner = text_player1.get()
            
            rounds_wonG1 += 1
            
        else:
            winner = text_player2.get()
            rounds_wonG2 += 1
        youwin()
        moves = {"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}#to reset the 
        #evaluators so the game doesnt remember pressed buttons from the previous game
        moves_count = -1
    elif moves["1"] == moves["5"] and moves["1"] == moves["9"]:
        
        if moves["1"] == gamer1:
            winner = text_player1.get()
            
            rounds_wonG1 += 1
            
        else:
            winner = text_player2.get()
            rounds_wonG2 += 1
        youwin()
        moves = {"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}#to reset the 
        #evaluators so the game doesnt remember pressed buttons from the previous game
        moves_count = -1
    elif moves["3"] == moves["5"] and moves["3"] == moves["7"]:
        
        if moves["3"] == gamer1:
            winner = text_player1.get()
            
            rounds_wonG1 += 1
            
        else:
            winner = text_player2.get()
            rounds_wonG2 += 1
        youwin()
        moves = {"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}#to reset the 
        #evaluators so the game doesnt remember pressed buttons from the previous game
        moves_count = -1
        
    moves_count += 1

def checkmatch():# In this function program checks winner and if its not check if its a tie after the 9 check. I had to
    #separate it to only check tie a the last move 
    
    if moves_count != 8:
        checkwinner()
    else:
        checkwinner()
        istie()
        
def entry_limiter_player1(entry_text_player1):
    if len(entry_text_player1.get()) > 0:
        mytext = entry_text_player1.get()[:6]
        entry_text_player1.set(mytext)
        
def entry_limiter_player2(entry_text_player2):
    if len(entry_text_player2.get()) > 0:
        mytext = entry_text_player2.get()[:6]
        entry_text_player2.set(mytext)

# ________________________________________________________________   
#|                                                                |
#|                     Game Variables                             |
#|________________________________________________________________|


#----------Raiz-----------------------
root = Tk()
root.title("Tic Tac Toe")
root.iconbitmap("juego tic icono.ico")
root.resizable(0,0)
image_bg = PhotoImage(file="juego tic fondo.gif")

#----------Frame------------------------

myframe = Frame()
myframe.pack()
myframe.config(width="650", height="350")
Label(myframe, image=image_bg).place(x=-2,y=0)
image_win = PhotoImage(file="well done board.gif")
image_tie = PhotoImage(file="tie board.gif")





#----------Board Buttons------------------------

button_00 = Button(myframe, width="9", height="4", bg="black", command=lambda:game_button_pressed("7"))
button_00.place(x=349, y=70 )
button_01 = Button(myframe, width="10", height="4", bg="black", command=lambda:game_button_pressed("8"))
button_01.place(x=430, y=70 )
button_02 = Button(myframe, width="9", height="4", bg="black", command=lambda:game_button_pressed("9"))
button_02.place(x=518, y=70 )
button_10 = Button(myframe, width="9", height="4", bg="black", command=lambda:game_button_pressed("4"))
button_10.place(x=349, y=150)
button_11 = Button(myframe, width="10", height="4", bg="black", command=lambda:game_button_pressed("5"))
button_11.place(x=430, y=150)
button_12 = Button(myframe, width="9", height="4", bg="black", command=lambda:game_button_pressed("6"))
button_12.place(x=518, y=150)
button_20 = Button(myframe, width="9", height="4", bg="black", command=lambda:game_button_pressed("1"))
button_20.place(x=349, y=230)
button_21 = Button(myframe, width="10", height="4", bg="black", command=lambda:game_button_pressed("2"))
button_21.place(x=430, y=230)
button_22 = Button(myframe, width="9", height="4", bg="black", command=lambda:game_button_pressed("3"))
button_22.place(x=518, y=230)

#----------------Variables-----------------------------------

game_start = 0
moves = {"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}# used to register the pressed 
#table buttons values so the logic can check the status
gamer1 = "x"#Used to check winner
gamer2 = "o"
winner = ""
turn_count = True 
rounds_wonG1 = 0
rounds_wonG2 = 0
moves_count = 0 # Used to check if tie
entry_text_player1 = StringVar()
entry_text_player1.trace("w", lambda name, index, mode, entry_text_player1=entry_text_player1: entry_limiter_player1(entry_text_player1))#lambda *args: entry_limiter(entry_text_player1)

entry_text_player2 = StringVar()
entry_text_player2.trace("w", lambda name, index, mode, entry_text_player2=entry_text_player2: entry_limiter_player2(entry_text_player2))#lambda *args: entry_limiter(entry_text_player1)





# _______________________________________________________
#|-------------------------------------------------------|
#|-------------Visual menus------------------------------|
#|_______________________________________________________|

#---------------------menu1------------------------------
    
label_tic = Label(myframe, text="TIC", bg="black", fg="white", font=("Broadway","40"))
label_tic.place(x=40, y=50)

label_tac = Label(myframe, text="TaC", bg="black", fg="white", font=("Broadway","40"))
label_tac.place(x=100, y=120)

label_toe = Label(myframe, text="Toe", bg="black", fg="white", font=("Broadway","40"))
label_toe.place(x=40, y=190)

start_button = Button(myframe, text="START", bg="gray", fg="black", relief="raised", font=("helvetica","20", "bold"))
start_button.config(bd=10, command=changetomenu2)
start_button.place(x=130, y=270)
    


#-----------Menu 2---------------------------------------------

label_player1 = Label(myframe, text="Player 1", bg="black", fg="white", font=("Broadway","20"))
label_player1.place()

text_player1 = Entry(myframe, textvariable = entry_text_player1)
text_player1.place()


label_x = Label(myframe, text="x", bg="black", fg="white", font=("helvetica","70"))
label_x.place()

label_player2 = Label(myframe, text="Player 2", bg="black", fg="white", font=("Broadway","20"))
label_player2.place()

text_player2 = Entry(myframe, textvariable = entry_text_player2)
text_player2.place()
    
label_o = Label(myframe, text="o", bg="black", fg="white", font=("helvetica","70"))
label_o.place()

ready_button = Button(myframe, text="Ready", bg="gray", fg="black", relief="raised", font=("helvetica","20", "bold"))
ready_button.config(bd=10, command=changetomenu3)
ready_button.place()

#------------Menu 3 Gamer turn-------------------------------------------------


 


label_turn = Label(myframe, text="TURN", bg="black", fg="white", font=("Broadway","50"))
label_turn.place()

#The name is changed in changetomenu3 funtion otherwise get() funtion get an empty Entry
m3label_player = Label(myframe, text=text_player1.get(), bg="black", fg="white", font=("Broadway","20"))
m3label_player.place()


label_big = Label(myframe, text=label_x.cget("text"), bg="black", fg="white", font=("helvetica","70"))#Crear una variable 
#para intercambiar la x por un o
label_big.place()

label_guide = Label(myframe, text="Select place on the board", bg="black", fg="white", font=("Broadway","10"))
label_guide.config(justify="center")
label_guide.place()

#-------------------Table labels appears when button is pressed------------------------
# to show the value between label x and o I use label big becouse it change every time a button is pushed.

label_00 = Label(myframe, bd="0",bg="black", fg="white", font=("helvetica",70))
label_00.place()
label_01 = Label(myframe, bd="0",bg="black", fg="white", font=("helvetica",70))
label_01.place()
label_02 = Label(myframe, bd="0",bg="black", fg="white", font=("helvetica",70))
label_02.place()
label_10 = Label(myframe, bd="0",bg="black", fg="white", font=("helvetica",70))
label_10.place()
label_11 = Label(myframe, bd="0",bg="black", fg="white", font=("helvetica",70))
label_11.place()
label_12 = Label(myframe, bd="0",bg="black", fg="white", font=("helvetica",70))
label_12.place()
label_20 = Label(myframe, bd="0",bg="black", fg="white", font=("helvetica",70))
label_20.place()
label_21 = Label(myframe, bd="0",bg="black", fg="white", font=("helvetica",70))
label_21.place()
label_22 = Label(myframe, bd="0",bg="black", fg="white", font=("helvetica",70))
label_22.place()

#------------------Win Windows and Scores----------------------------------------------

label_win = Label(myframe, bd="0",bg="black", fg="white", font=("helvetica",70))# Shows image win or tie when match ends
label_win.place()

label_win_name = Label(myframe, bd="0",bg="black", fg="white", font=("helvetica",35))
label_win_name.config(justify="center")
label_win_name.place()

label_scores = Label(myframe, text="Scores", bd="0",bg="black", fg="white", font=("helvetica",25))#text_player1.get
label_scores.place()

label_win1 = Label(myframe, bd="0",bg="black", fg="white", font=("helvetica",20))#text_player1.get
label_win1.place()
label_win1pts = Label(myframe, bd="0",bg="black", fg="white", font=("helvetica",20))#text_player1.get
label_win1pts.place()

label_win2 = Label(myframe, bd="0",bg="black", fg="white", font=("helvetica",20))#text=text_player2.get
label_win2.place()
label_win2pts = Label(myframe, bd="0",bg="black", fg="white", font=("helvetica",20))#text=text_player2.get
label_win2pts.place()

different_players_button = Button(myframe, text="New Players", bg="gray", fg="black", relief="raised", font=("helvetica","7", "bold"))
different_players_button.config(bd=10, command=changetomenu2)
different_players_button.place()

new_game_button = Button(myframe, text="New Game", bg="gray", fg="black", relief="raised", font=("helvetica","7", "bold"))
new_game_button.config(bd=10, command=changetomenu3)
new_game_button.place()


#-----------------------------------------------------------------------------------

root.mainloop()