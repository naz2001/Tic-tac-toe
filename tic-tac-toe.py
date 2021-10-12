global board
board=[[" "," "," "],[" "," "," "],[" "," "," "]]
player = "X"

#print board
def printBoard(board):
    for line in board:
         print(line)
#take in input and replace the appropriate space in the grid
def move():
    global player
    x = int(input("Player " + player + ", What is the x cordinate "))
    y = int(input("\tWhat is the y cordinate "))
    
    while board[x][y] != " ":
        print("You must choose an empty spot")
        x = int(input("Player " + player + ", What is the x cordinate "))
        y = int(input("\tWhat is the y cordinate "))
    #board[y][x] = "X"
    if player =="X":
       board[y][x] = "X"
       player = "O"
    else:   
        board[y][x] = "O"
        player = "X"

#check if there is a winner
def iswin():
    global player
    if player == "X":
        p = "O"
    else:
        p = "X"   
    #row
    for c in range (len(board)):
        win =True
        for r in range (len(board)):
            if board[c][r] != p:
                win= False
                break
        if win:
            print("Player " + p + " won!!")
            return True    

    #column
    for c in range (len(board)):
        win =True
        for r in range (len(board)):
            if board[r][c] != p:
                win= False
                break
        if win:
            print("Player " + p + " won!!")
            return True 
    #diagonals
    win =True
    for r in range (len(board)):
        if board[c][c] != p:
            win= False
            break
        if win:
            print("Player " + p + " won!!")
            return True 
    win =True
    for r in range (len(board)):
        if board[r][len(board)-1-r] != p:
            win= False
            break
        if win:
            print("Player " + p + " won!!")
            return True 

    return False


def tic() :
    printBoard(board)
    move()
    iswin()
   

def main():
    gamewon = False
    while gamewon ==False:
        tic()
        gamewon = iswin() 
    printBoard(board) 
    print("Game Over")  


main()