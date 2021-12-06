import numpy as np
from functions import diagnosticReport


def opentxt(string):
    lines = []
    with open(string) as f:
        lines = f.readlines()
    return lines


def playBingo(boards,randomDraws,nr,nrOfBoards):

    #TODO continue program for all randomDraws and check for winner
    i=0
    finalNumber = -1
    while(checkWinner(boards, finalNumber) and i < nr):
        for board in boards:
            for row in board:
                for number in row:
                    if number["number"] == int(randomDraws[i]):
                        number["marked"] = True
        #print(randomDraws[i])

        #finalBoard  = board
        finalNumber = int(randomDraws[i])
        #print(i, randomDraws[i])
        i+=1
    #print(finalBoard[0])
    #print(finalBoard[1])
    #print(finalBoard[2])
    #print(finalBoard[3])
    #print(finalBoard[4])
    score = 0
    #for row in finalBoard:
      #  for num in row:
      #      if not num["marked"]:
      #          score += num["number"]

    finalBoard = retrieveWinner(boards)
    score = calculateScore(finalBoard,finalNumber)
    print(f"final number = {finalNumber}, {finalBoard}, score = {score}")
    return retrieveWinner(boards)

def retrieveWinner(boards):
    for board in boards:
        for i in range(len(board)):
            bingoRow = 0
            bingoCol = 0
            for j in range(len(board)):
                if board[i][j]["marked"]:
                    bingoRow+=1
                if board[j][i]["marked"]:
                    bingoCol+=1
                    #print(j,i, board[j][i]["number"])
                if bingoRow > 4 or bingoCol > 4:
                    return board
def calculateScore(board,finalNumber):
    score = 0
    for row in board:
        for num in row:
            if not num["marked"]:
                score += num["number"]
    #print(board[0])
    #print(board[1])
    #print(board[2])
    #print(board[3])
    #print(board[4])
    print(score*finalNumber)
    return score*finalNumber
def checkWinner(boards,finalNumber):
    for board in boards:
        for i in range(len(board)):
            bingoRow = 0
            bingoCol = 0
            for j in range(len(board)):
                if board[i][j]["marked"]:
                    bingoRow+=1
                if board[j][i]["marked"]:
                    bingoCol+=1
                    #print(j,i, board[j][i]["number"])
                if bingoRow > 4 or bingoCol > 4:
                    #print("Bingo")
                    #print(bingoRow, bingoCol)
                    #print(board)
                    calculateScore(board,finalNumber)
                    return False
    return True
if __name__ == '__main__':
    lines = opentxt("bingoInput.txt")
    randomDraws = lines[0].split(",")
    nr = len(randomDraws)
    boardLines = lines[2:]
    nrOfBoards = int((len(boardLines) + 1) / 6)
    # print(boardLines)
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


    while(True):
        winner = playBingo(boards,randomDraws,nr,nrOfBoards)
        for row in winner:
            for num in row:
                num["marked"] = False
        boards.remove(winner)
        nrOfBoards = len(boards)
        print("nrBoards = ",nrOfBoards)