lines = []
with open("Days/Day4/bingoInputTest.txt") as f:
    lines = f.readlines()


randomDraws = lines[0].split(",")
print(len(randomDraws))
#print(randomDraws)
boardLines = lines[2:]
nrOfBoards = int((len(boardLines)+1) / 6)
print(nrOfBoards)
#print(boardLines)
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
print(boards)