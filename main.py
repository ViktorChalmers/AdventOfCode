import numpy as np
from functions import diagnosticReport


def opentxt(string):
    lines = []
    with open(string) as f:
        lines = f.readlines()
    return lines


def playBingo(lines):
    randomDraws = lines[0]
    boardLines = lines[2:]
    nrOfBoards = int((len(boardLines) - 1) / 5)

    boards = [[[
        {
            "bingo": False,
            "number": int(
                boardLines[j + k * 6].replace(" ", ",").replace(",,", ",").replace(",", " ").strip().split(" ")[i])
        }
        for i in range(5)
    ]
        for j in range(5)
    ]
        for k in range(nrOfBoards)
    ]
    #TODO continue program for all randomDraws and check for winner
    for board in boards:
        for row in board:
            for number in row:
                if number["number"] == int(randomDraws[0]):
                    number["bingo"] = True
    print(randomDraws[0])
    print(boards[2][4][4])

if __name__ == '__main__':
    lines = opentxt("bingoInputTest.txt")
    playBingo(lines)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
