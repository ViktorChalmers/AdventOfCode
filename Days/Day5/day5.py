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
    with open('input.txt') as f:
        lines = f.readlines()

    x1,x2,y1,y2 = [],[],[],[]
    for line in lines:
        x1.append(int(line.split("->")[0].split(",")[0]))
        x2.append(int(line.split("->")[1].split(",")[0]))
        y1.append(int(line.split("->")[0].split(",")[1]))
        y2.append(int(line.split("->")[1].split(",")[1]))


    for i in range(len(x1)):
        x1[i],x2[i] = min(x1[i],x2[i]),max(x1[i],x2[i])
        y1[i],y2[i] = min(y1[i],y2[i]),max(y1[i],y2[i])

    state = np.zeros([1000,1000])
    for k in range(len(x1)):
    #k = 1
        #print(f"{x1[k]},{y1[k]} -> {x2[k]},{y2[k]}")
        if y1[k] == y2[k]:
            for i in range(x1[k],x2[k]+1):
                state[y1[k],i] += 1
        if x1[k] == x2[k]:
            for i in range(y1[k],y2[k]+1):
                state[i,x1[k]] += 1


    #print(state)
    crosspoints = len(np.where(state>1)[0])
    #print(crosspoints)

    with open('input.txt') as f:
        lines = f.readlines()

    x1,x2,y1,y2 = [],[],[],[]
    for line in lines:
        x1.append(int(line.split("->")[0].split(",")[0]))
        x2.append(int(line.split("->")[1].split(",")[0]))
        y1.append(int(line.split("->")[0].split(",")[1]))
        y2.append(int(line.split("->")[1].split(",")[1]))

    for k in range(len(x1)):
        if x1[k] != x2[k] and y1[k] != y2[k]:
            dx = x2[k]-x1[k]
            dy = y2[k]-y1[k]
            if y1[k]>y2[k]:
                x1[k],y1[k],x2[k],y2[k] = x2[k],y2[k],x1[k],y1[k]
            if y1[k]<y2[k]:
                for i in range((y2[k]-y1[k])+1):
                    if x1[k]<x2[k]:
                        state[y1[k] + i, x1[k] + i] += 1
                    else:
                        state[y1[k] + i, x1[k] - i] += 1
            elif x1[k]<x2[k]:
                for i in range((x2[k]-x1[k])+1):
                    if x1[k] < x2[k]:
                        state[y1[k] + i, x1[k] + i] += 1
                    else:
                        state[y1[k] - i, x1[k] + i] += 1
    #print(state)
    crosspoints = len(np.where(state > 1)[0])
    print(crosspoints)