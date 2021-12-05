import numpy as np

def commandInput(string = "inputCommand.txt"):

    lines = []
    with open(string) as f:
        lines = f.readlines()
    countFor = 0
    countUp = 0
    aim = 0
    for line in lines:
        x = line.split(" ")
        if x[0] == "forward":
            countFor = countFor + int(x[1])
            countUp += aim*int(x[1])
        if x[0] == "up":
            aim -= int(x[1])
        if x[0] == "down":
            print(x)
            aim += int(x[1])
    print(countUp*countFor)

def calculateNrOfIncrement(dataArray: np.ndarray):
    difference = np.diff(dataArray)
    return np.sum(np.array(difference) > 0, axis=0)

def flatList(dataArray: np.ndarray):
    sum = np.zeros(len(dataArray)-2)
    for i in range(len(dataArray)-2):
        sum[i] = np.sum(dataArray[i:i+3])
    return sum

def arrayToString(array):
    arrayString = ""
    for num in array:
        arrayString += str(num)
    return arrayString

def binaryToDecimal(n):
    return int(n,2)

def diagnosticReport(lines,type):
    if type == "PC":
        binLength = len(lines[0])
        gamma = np.zeros(binLength-1)
        epsilon = np.zeros(binLength - 1)

        for i in range(binLength-1):
            one = 0
            zero = 0
            for line in lines:
                if int(line[i]) == 0:
                    zero += 1
                elif int(line[i]) == 1:
                    one += 1
            if one > zero:
                gamma[i] = 1
                epsilon[i] = 0
            elif one < zero:
                gamma[i] = 0
                epsilon[i] = 1
        print(str(2))
        gamma = gamma.astype(int)
        epsilon = epsilon.astype(int)
        gammaDec = binaryToDecimal(arrayToString(gamma))
        epsilonDec = binaryToDecimal(arrayToString(epsilon))
        print(gammaDec*epsilonDec)
    elif type == "LSR":
        tmp = []
        for j in range(2):
            tempLines = lines
            for i in range(len(tempLines[0])-1):
                if len(tempLines) == 1:
                    break
                one = 0
                zero = 0
                tempOxygen = []
                tempCO2 = []

                for line in tempLines:
                    if int(line[i]) == 1:
                        one += 1
                    if int(line[i]) == 0:
                        zero += 1
                if one>=zero:
                    for line in tempLines:
                        if int(line[i]) == 1-j:
                            tempOxygen.append(line)
                elif zero>one:
                    for line in tempLines:
                        if int(line[i]) == j:
                            tempOxygen.append(line)
                tempLines = tempOxygen
            tmp.append(tempLines)
        print(binaryToDecimal(arrayToString(tmp[0]))*binaryToDecimal(arrayToString(tmp[1])))
    else:
        print("choose type")