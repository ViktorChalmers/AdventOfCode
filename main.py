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
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test = np.loadtxt("input.txt")
    #inputCommand = np.loadtxt("inputCommand.txt")
    sum = flatList(test)
    #commandSubmarine(inputCommand)

    lines = []
    with open('inputCommand.txt') as f:
        lines = f.readlines()

    countFor = 0
    countUp = 0
    aim = 0
    for line in lines:
        x = line.split(" ")
        if x[0] == "forward":
            countFor = countFor + int(x[1])
        if x[0] == "up":
            countUp = countUp +  int(x[1])
        if x[0] == "down":
            print(x)
            countUp = countUp -int(x[1])
    print(countUp*countFor)
        #print(f'line {count}: {line}')
        #print(calculateNrOfIncrement(sum))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
