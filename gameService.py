from winnerStatus import winnerStatus
winPositions = []
def CalculateWinner(inputMoves):
    """Populates gameboard to calculate winner"""
    gameBoard = {}
    i = 0
    for move in inputMoves:
        gameBoard[i] = move
        i+=1
    winPositions.clear()
    return getPositions(gameBoard)

def getPositions(moveDict):
    """Obtains position of X and O values in the gameboard"""
    noWinner = []
    winner = winnerStatus(False, noWinner, "N")
    xPositions = []
    oPositions = []
    for key, value in moveDict.items():
        if value == "X":
            xPositions.append(key)
        elif value == "O":
            oPositions.append(key)
 
    xWin = isWinner(xPositions)
    oWin = isWinner(oPositions)

    if(xWin):
        winner = winnerStatus(True, winPositions, "X")  
    elif(oWin):
        winner = winnerStatus(True,winPositions,"O")
    return winner.asdict()
    

def leftDiagonalWinCheck(startingPosition):
    for i in range(7):
        if(startingPosition == (7*i) or startingPosition == 1 + (7*i) or startingPosition == 2+(7*i)):
            return False
    return True

def rightDiagonalWinCheck(startingPosition):
    for i in range(7):
        if(startingPosition == 4+(7*i) or startingPosition == 5 + (7*i) or startingPosition == 6+(7*i)):
            return False
    return True    
            
def isWinner(movePositions):
    for i in movePositions:
        verticalWin = i+7 in movePositions and i+14 in movePositions and i+21 in movePositions
        rightDiagonalWin = i+8 in movePositions and i+16 in movePositions and i+24 in movePositions
        horizontalWin = i+1 in movePositions and i+2 in movePositions and i+3 in movePositions
        leftDiagonalWin = i+6 in movePositions and i+12 in movePositions and i+18 in movePositions

        if verticalWin:
            winPositions.append(i)
            winPositions.append(i+7)
            winPositions.append(i+14)
            winPositions.append(i+21)
            return True
        if rightDiagonalWinCheck(i):
            if rightDiagonalWin:
                winPositions.append(i)
                winPositions.append(i+8)
                winPositions.append(i+16)
                winPositions.append(i+24)
                return True
            elif horizontalWin:
                winPositions.append(i)
                winPositions.append(i+1)
                winPositions.append(i+2)
                winPositions.append(i+3)
                return True
        if leftDiagonalWinCheck(i):
            if leftDiagonalWin:
                winPositions.append(i)
                winPositions.append(i+6)
                winPositions.append(i+12)
                winPositions.append(i+18)
                return True
    return False

    