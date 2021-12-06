import numpy as np
from functions import diagnosticReport


def opentxt(string):
    lines = []
    with open(string) as f:
        lines = f.readlines()
    return lines


def playBingo(lines):
    randomDraws = lines[0].split(",")
    print(randomDraws)
    boardLines = lines[2:]
    nrOfBoards = int((len(boardLines)+1) / 6)
    print(boardLines)
    boards = [[[
        {
            "marked": False,
            "number": int(
                            boardLines[j + k * 6].replace(" ", ",").replace(",,", ",").replace(",", " ").strip().split(" ")[i]
                         )
        }
        for i in range(5)
    ]
        for j in range(5)
    ]
        for k in range(nrOfBoards)
    ]
    #TODO continue program for all randomDraws and check for winner
    i=0
    while(checkWinner(boards) and i < 13):
        for board in boards:
            for row in board:
                for number in row:
                    if number["number"] == int(randomDraws[i]):
                        number["marked"] = True
        #print(randomDraws[i])
        finalBoard  = board
        finalNumber = int(randomDraws[i])
        print(i, randomDraws[i])
        i+=1
    print(finalBoard)
    score = 0
    for row in finalBoard:
        for num in row:
            if not num["marked"]:
                score += num["number"]
    print(score*finalNumber)
    #print(boards[2][0])

def checkWinner(boards):
    for board in boards:
        for i in range(len(board)):
            bingoRow = 0
            bingoCol = 0
            for j in range(len(board)):
                if board[i][j]["marked"]:
                    bingoRow+=1
                if board[j][i]["marked"]:
                    bingoCol+=1
                if bingoRow>4 or bingoCol > 4:
                    #print(board)
                    return False
    return True
if __name__ == '__main__':
    lines = opentxt("bingoInput.txt")
    playBingo(lines)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
