print("Hello")

def printGameTable(table):
    for i in range(len(table)):
        print(" ---------")
        print(" ", end = "")
        for j in range(len(table[i])):
            if((j + 1) % 3 != 0):
                print(table[i][j] + " | ", end = "")
            else:
                print(table[i][j])
        
    print(" ---------")

def XMakeChoice(table):
    print("Please choose position for X: ")
    x, y = [int(x) for x in input("Enter two values: ").split()]
    table[x][y] = "X"

def OMakeChoice(table):
    print("Please choose position for O: ")
    x, y = [int(x) for x in input("Enter two values: ").split()]
    table[x][y] = "O"

def transponateMatrix(table):
    newTable = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]

    for i in range(len(table)):
        for j in range(len(table[i])):
            newTable[i][j] = table[j][i]
    return newTable

def anyoneWon(table):
    for i in range(len(table)):
        if(table[i][0] == table[i][1] and table[i][1] == table[i][2] and (table[i][0] == "X" or table[i][0] == "O")):
            return (" " + table[i][0] + " won")
        
    if(table[0][0] == table[1][1] and table[1][1] == table[2][2] and (table[0][0] == "X" or table[0][0] == "O")):
        return (" " + table[0][0] + " won")
    
    newTable = transponateMatrix(table)

    for i in range(len(newTable)):
        if(newTable[i][0] == newTable[i][1] and newTable[i][1] == newTable[i][2] and (newTable[i][0] == "X" or newTable[i][0] == "O")):
            return (" " + newTable[i][0] + " won")
    
    return 0



gameArray = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]


counter = 0

while(1):
    printGameTable(gameArray)
    XMakeChoice(gameArray)

    if(anyoneWon(gameArray) != 0):
        printGameTable(gameArray)
        print(anyoneWon(gameArray))
        break

    if(counter == 8):
        printGameTable(gameArray)
        print("Tie!!!")
        break

    printGameTable(gameArray)
    OMakeChoice(gameArray)

    if(anyoneWon(gameArray) != 0):
        printGameTable(gameArray)
        print(anyoneWon(gameArray))
        break

    counter += 2

    
    

