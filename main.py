import numpy as np
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def calculateNrOfIncrement(dataArray: np.ndarray):
    difference = np.diff(dataArray)
    return np.sum(np.array(difference) > 0, axis=0)

def flatList(dataArray: np.ndarray):
    sum = np.zeros(len(dataArray)-2)
    for i in range(len(dataArray)-2):
        sum[i] = np.sum(dataArray[i:i+3])
    return sum

def commandSubmarine(command):
    print(command)

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
            #countUp = countUp +  int(x[1])
        if x[0] == "down":
            print(x)
            aim += int(x[1])
            #countUp = countUp -int(x[1])
    print(countUp*countFor)
        #print(f'line {count}: {line}')
        #print(calculateNrOfIncrement(sum))
# Press the green button in the gutter to run the script.

def diagnosticReport(string = "diagnosticReportTest.txt"):
    dRep = np.loadtxt("diagnosticReportTest.txt")
    print(dRep)

    lines = []
    with open(string) as f:
        lines = f.readlines()
    binLength = len(lines[0])
    print(binLength-1)
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
    print(gamma, epsilon)
if __name__ == '__main__':
    diagnosticReport()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
