import numpy as np
import matplotlib.pyplot as plt
from functions import diagnosticReport
from io import StringIO   # StringIO behaves like a file object

def updateState(state,points):
    if points[0] == points[1]:
        print(f"column update, {points[0]},{points[2]} -> {points[1]},{points[3]}")
        state[points[2]:points[3],points[0]] += 1
    if points[2] == points[3]:
        print(f"row update, {points[0]},{points[2]} -> {points[1]},{points[3]}")
        state[points[2],points[0]:points[1]] += 1
    #print(state)
    return state

if __name__ == '__main__':
    with open('inputTest.txt') as f:
        lines = f.readlines()

    x1,x2,y1,y2 = [],[],[],[]
    for line in lines:
        x1.append(int(line.split("->")[0].split(",")[0]))
        x2.append(int(line.split("->")[1].split(",")[0]))
        y1.append(int(line.split("->")[0].split(",")[1]))
        y2.append(int(line.split("->")[1].split(",")[1]))
    print(x1)
    print(x2)
    print(y1)
    print(y2)
    lattice = 10

    for i in range(len(x1)):
        x1[i],x2[i] = max(x1[i],x2[i]),min(x1[i],x2[i])
        x1[i], x2[i] = max(x1[i], x2[i]), min(x1[i], x2[i])
    #for i in range(len(x1)):
    #    print(x1[i],x2[i],y1[i],y2[i])
    #    if x1[i] == x2[i] or y1[i]==y2[i]:
    #        plt.plot([x1[i],x2[i]],[y1[i],y2[i]])


    #state = np.zeros([11,11])
    #for i in range(len(x1)):
    #    state = updateState(state,[x1[i],x2[i],y1[i],y2[i]])

    #print(state)
    #plt.show()