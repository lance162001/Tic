import random
board=[['_','_','_','_'],['_','_','_','_'],['_','_','_','_'],['_','_','_','_']]
default=board
Win=False
Loss=False
Stalemate=False
class Ai():
    def __init__(self):
        pass
    def readBoard(self):
        self.board=[]
        for lists in board:
            for items in lists:
                self.board.append(items)
#Strategy #1
#Checks for open spots, and picks one at random. Is the fallback if the bot doesn't know how to react.
    def random(self):
        if self.choice != True:
            repeat=True
            while repeat == True:
                x=random.randint(1,16)
                x-=1
                if self.board[x] == "_":
                    repeat=False
            self.board[x]="0"
            return(self.compile())
        else:
            return (board)
#Strategy #2
#Prevents basic and obvious losses, but still has no offensive strategy unless already
#in a winning position and doesn't think ahead at all.
#Tests for all ways for the player to win and itself to win,
#and reacts if the player is one move from winning by blocking them.
    def simple(self):
        self.choice=False
        for rows in board:
            self.rowDanger=0
            for space in rows:
                if space == "x":
                    self.rowDanger+=1
                if space == "0":
                    self.rowDanger-=1
            if self.rowDanger == 3 or self.rowDanger == -3:
                print("horizontal detected")
                self.choice=True
                rows.insert(rows.index("_"),"0")
                rows.remove("_")
                break
        if self.choice == False:
            for i in range(4):
                self.rowDanger=0
                for rows in board:
                    if rows[i] == "x":
                        self.rowDanger+=1
                    if rows[i] == "0":
                        self.rowDanger-=1
                if self.rowDanger == 3 or self.rowDanger == -3:
                    for rows in board:
                        if rows[i] == "_":
                            rows[i]="0"
                    print("vertical detected")
                    self.choice=True
                    break

        if self.choice == False:
            diagonal=[self.board[0],self.board[5],self.board[10],self.board[15]]
            diagonal2=[self.board[3],self.board[6],self.board[9],self.board[12]]
            for diagonals in (diagonal,diagonal2):
                self.rowDanger=0
                for i in diagonals:
                    if i == "x":
                        self.rowDanger+=1
                    if i == "0":
                        self.rowDanger-=1
                if self.rowDanger == 3 or self.rowDanger == -3:
                    print("diagonal detected")
                    self.choice=True
                       
        if self.choice == True:
            print("Bot is responding to immediate danger or is about to win.")

    def compile(self):
        return([list(self.board[0:4]),list(self.board[4:8]),list(self.board[8:12]),list(self.board[12:16])])

ai=Ai()

def displayBoard():
    temp="A B C D\n\n"
    x=1
    for i in board:
        for space in i:
            temp+=space
            temp+=" "
        temp+="  "
        temp+=str(x)
        x+=1
        if (board.index(i)+1) != len(board):
            temp+="\n"
    return(temp)

def updateBoard(x,y):
    if board[y-1][x-1] == "_":
        board[y-1][x-1]="x"
        return(False)
    else:
        return(True)

print("A 4x4 Tic-Tac-Toe bot that has a simple strategy but doesn't miss anything\nDeveloped by Lance Gruber\n\n")

#Loop that keeps turns going until the game ends.
    
while Win == False and Loss == False and Stalemate == False:

#UI and User Input

    print("____________\n",displayBoard(),"____________\n")

    error=False
    x=input("A, B, C or D? : ")
    if x == "A":
        x=1
    elif x == "B":
        x=2
    elif x == "C":
        x=3
    elif x == "D":
        x=4
    y=input("1, 2, 3, or 4? : ")

#Updating Board

    repeat=updateBoard(int(x),int(y))

#Bot Response (only triggers random if the simple function yields no updated board)
    
    tempboard=list(board)
    if repeat == False:
        ai.readBoard()
        ai.simple()
        if tempboard == board:
            board=ai.random()

#Checking horizontally for a win

    checkWin=True
    checkLoss=True
    for i in board:
        for spots in i:
            if spots!="x":
                checkWin=False
            if spots!="0":
                checkLoss=False
        if checkWin == True:
            print("horizontal win")
            Win=True
            break
        elif checkLoss == True:
            print("horizontal loss")
            Loss=True
            break
        checkWin=True
        checkLoss=True

#Checking vertically for a win


    checkWin=True
    checkLoss=True
    for i in range(4):
        for lists in board:
            if lists[i]!="x":
                checkWin=False
            if lists[i]!="0":
                checkLoss=False
        if checkWin==True:
            print("vertical win")
            Win=True
            break
        if checkLoss==True:
            print("vertical loss")
            Loss=True
            break
        checkWin=True
        checkLoss=True

#Checking Diagonally for a win
        
    if (board[0][0]=="x" and board[1][1]=="x" and board[2][2]=="x" and board[3][3]=="x") or (board[0][3]=="x" and board[1][2]=="x" and board[2][1]=="x" and board[3][0]=="x"):
        print("diagonal win")
        Win=True
    elif (board[0][0]=="0" and board[1][1]=="0" and board[2][2]=="0" and board[3][3]=="0") or (board[0][3]=="0" and board[1][2]=="0" and board[2][1]=="0" and board[3][0]=="0"):
        print("diagonal loss")
        Loss=True
        
#Checking for a stalemate
        
    Stalemate=True
    for lists in board:
        for i in lists:
            if i == "_":
                Stalemate=False

#EndGame 

print(displayBoard(),"\nGame Over!")
if Win == True:
    print("You Won !")
elif Loss == True:
    print("You Lost..")
elif Stalemate == True:
    print("Stalemate...")
else:
    print("Error: Unknown final game state")
